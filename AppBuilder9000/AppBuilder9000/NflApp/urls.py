from django.urls import path
from . import views

urlpatterns = [
    path('', views.Nfl_home, name='NflHome'),
    path('createPlayer', views.createPlayer, name='createPlayer'),
    path('NflApp_index', views.NflApp_index, name='NflApp_index'),
    path('<int:pk>/NflApp_details/', views.NflApp_details, name='NflApp_details'),
    path('<int:pk>/NflApp_edit/', views.NflApp_edit, name='NflApp_edit'),
    path('<int:pk>/NflApp_delete/', views.NflApp_delete, name='NflApp_delete'),
]