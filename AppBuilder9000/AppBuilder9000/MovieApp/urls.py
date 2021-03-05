from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='MovieAppHome'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('movieapp_index/', views.movieapp_index, name='movieapp_index'),
    path('movieapp_details/<int:pk>/', views.movieapp_details, name='movieapp_details'),
]