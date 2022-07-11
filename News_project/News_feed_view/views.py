from django.views.generic import ListView, DetailView
from .models import News
from .filters import NewsFilter


class NewsList(ListView):
    model = News # model what are we going to view
    template_name = 'news.html' # where are we going to do it
    ordering = 'name'
    context_object_name = 'news' # where are we going to contain our objects to go to list of objects of HTML
    paginate_by = 2


class SearchNews(ListView):
    model = News
    template_name = 'search.html'
    context_object_name = 'search_news'
    ordering = ['datetime_pub']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return NewsFilter(self.request.GET, queryset=queryset).qs


class NewsDetails(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'current_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'current_news'


