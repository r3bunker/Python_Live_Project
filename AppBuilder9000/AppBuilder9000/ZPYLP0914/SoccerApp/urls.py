from django.urls import path
from . import views

urlpatterns = [
    path('', views.soccer_home, name='SoccerAppHome'),
    path('add', views.Addplayer, name='add'),
    path('Submit', views.Submit, name='Submit'),
    path('<int:pk>/details/', views.details, name='Details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]