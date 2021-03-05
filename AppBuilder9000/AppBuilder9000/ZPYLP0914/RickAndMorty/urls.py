from django.urls import path
from . import views

urlpatterns = [
    path('', views.rickandmorty_home, name='RickAndMorty_home'),
    path('add_character', views.add_character, name='add_character'),
    path('rick_index', views.index, name='rick_index'),
    path('<int:pk>/RickAndMorty_details', views.details, name='details'),
    path('<int:pk>/RickAndMorty_update', views.update, name='update'),
    path('<int:pk>/RickAndMorty_delete', views.delete, name='delete'),
    path('RickAndMorty_api_search/', views.api_search, name='api_search'),
    path('oops', views.oops, name='oops'),
    path('bios', views.bs_search, name='bios')
]