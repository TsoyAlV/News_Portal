from .views import NewsList, NewsDetails
from django.urls import path


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetails.as_view())
]