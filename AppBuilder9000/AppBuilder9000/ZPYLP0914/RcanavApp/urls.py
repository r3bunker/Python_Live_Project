from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('home', views.Central_Africa_Republic_home, name='CARHome'),
    path('thingstodo', views.thingstodo, name='Thingstodo'),
    path('savecities', views.save_cities, name='SaveCities'),
    path('wish_index', views.cities_wish_list_index, name='WishList'),
    path('hotels', views.cities_hotels, name='Hotels'),
    path('citiesDetails/<int:pk>/', views.cities_details, name='save_cities'),
    path('citiesDelete/<int:pk>/', views.delete, name='deleteCity'),
    path('citiesEdit/<int:pk>/', views.edit, name='editCity'),
    path('cities-details/<int:pk>/', views.cities_details, name='save_cities'),
    path('tickets', views.api_response, name='api')


]