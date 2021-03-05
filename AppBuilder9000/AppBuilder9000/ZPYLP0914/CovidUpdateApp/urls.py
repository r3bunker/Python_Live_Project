from . import views
from django.urls import path

urlpatterns = [
    path('', views.Covidhome, name='Covidhome'),
    path('contact', views.contact, name='ContactForm'),
    path('index', views.covidIndex, name='covidIndex'),
    path('inputDetails/<int:pk>/', views.inputDetails, name='inputDetails'),
]
