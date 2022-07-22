from .views import NewsList, NewsDetails, SearchNews, NewsCreateView, NewsDeleteView, NewsUpdateView
from django.urls import path


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetails.as_view(), name = 'news_detail'),
   path('search_news/', SearchNews.as_view(), name = 'search_news'),
   path('news_create/', NewsCreateView.as_view(), name = 'create_news'),
   path('delete_news/<int:pk>/', NewsDeleteView.as_view(), name = 'delete_news'),
   path('update_news/<int:pk>/', NewsUpdateView.as_view(), name = 'update_news'),


]