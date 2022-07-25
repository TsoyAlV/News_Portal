from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .forms import NewsForm
from .filters import NewsFilter, NewsSimpleFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class NewsList(ListView):
    model = News # model what are we going to view
    template_name = 'news.html' # where are we going to do it
    ordering = 'name'
    context_object_name = 'news_list' # where are we going to contain our objects to go to list of objects of HTML
    paginate_by = 5

    # Для простого поиска:
    def get_queryset(self):
        queryset = super().get_queryset()
        return NewsFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetails(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'current_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'current_news'



class SearchNews(ListView):
    model = News
    template_name = 'search_news.html'
    ordering = 'name'
    context_object_name = 'search_news'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return NewsSimpleFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsSimpleFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        # берём значения для нового товара из POST-запроса, отправленного на сервер
        name = request.POST['name']
        category_id = request.POST['category']
        content = request.POST['content']
        date_pub = request.POST['date_pub']
        news = News(name=name, category_id=category_id, content = content, date_pub = date_pub)  # создаём новый товар и сохраняем
        news.save()
        return super().get(request, *args, **kwargs)


class NewsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('News_feed_view.create_News')
    template_name = 'news_create.html'
    form_class = NewsForm



class NewsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    permission_required = ('News_feed_view.change_News')

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk = id)

# дженерик для удаления товара
class NewsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('News_feed_view.delete_News')
    template_name = 'news_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'


