from django.urls import path
from . import views

urlpatterns = [
    path('', views.d_and_d_home, name='DandDHome'),
    path('add_character', views.add_character, name='add_character'),
    path('d_and_d_index', views.d_and_d_index, name='d_and_d_index'),
    path('<int:pk>/', views.d_and_d_details, name='d_and_d_details'),

]
