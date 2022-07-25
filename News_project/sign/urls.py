from .views import IndexView, upgrade_me, do_author
from django.urls import path


urlpatterns = [
   path('index/', IndexView.as_view(), name = 'personal_page'),
   path('upgrade/', upgrade_me, name = 'upgrade'),
   path('do_author/', do_author, name = 'do_author')
]