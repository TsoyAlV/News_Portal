from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News # model what are we going to view
    template_name = 'news.html' # where are we going to do it
    ordering = 'name'
    context_object_name = 'news' # where are we going to contain our objects to go to list of objects of HTML


class NewsDetails(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'current_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'current_news'


