from django.urls import path

from . import views

urlpatterns = [
    path('', views.NSW_APP_Homepage, name="NSWAppHome"),
    path('About/', views.NSW_APP_About, name="NSWAppAbout"),
    path('', views.NSW_News_API, name="NSWNewsSearchAPI"),
    path('Current_Games_Index/', views.Current_Games_Index, name="CurrentGamesIndex"),
    path('Future_Games_Index/', views.Future_Games_Index, name="FutureGamesIndex"),
    path('User_Library/Add_Game', views.Add_Game, name="AddGame"),
    path('User_Library/', views.User_Library, name="UserLibrary"),
    path('User_Library/details/<int:pk>/', views.Details, name="GameDetails")
]