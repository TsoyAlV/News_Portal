from .views import NewsList, NewsDetails, SearchNews, NewsCreateView, NewsDeleteView, NewsUpdateView
from django.urls import path


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetails.as_view(), name = 'news_detail'),
   path('search_news/', SearchNews.as_view(), name = 'search_news'),
   path('create_news/', NewsCreateView.as_view(), name = 'create_news'),
   path('delete_news/', NewsDeleteView.as_view(), name = 'delete_news'),
   path('update_news/', NewsUpdateView.as_view(), name = 'update_news'),


]