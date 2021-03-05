from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='PokeDexHome'),
    path('Report', views.Sighting, name='PokeDex_sightings'),
    path('sightings', views.report, name='PokeDex_report'),
    path('Details/<int:pk>/', views.details, name='PokeDex_details')
]
