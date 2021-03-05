from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='CatchIdentificationAppHome'),
    path('contact', views.contact, name='ContactForm'),
    path('theBigOne', views.catchLog, name='BigOne'),
   # path('catchindex', views.catchindex, name='catchIndex'),
    path('catchindex', views.searchlog, name='searchlog'),
]