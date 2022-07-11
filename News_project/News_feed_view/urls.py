from .views import NewsList, NewsDetails, SearchNews
from django.urls import path


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetails.as_view()),
   path('search/', SearchNews.as_view()),
]