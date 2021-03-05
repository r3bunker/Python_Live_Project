from django.urls import path
from . import views

urlpatterns = [
    path('', views.SOS_home, name='SoundsOfSpace'),
    path('add_star', views.add_star, name='add_star'),
    path('add_planet', views.add_planet, name='add_planet'),
    path('add_moon', views.add_moon, name='add_moon'),
    path('SOS_PlanetIndex', views.PlanetIndexPage, name='SOS_PlanetIndex'),
    path('SOS_PlanetIndex/<int:id>', views.PlanetDetailPage, name='SOS_PlanetDetail'),
]