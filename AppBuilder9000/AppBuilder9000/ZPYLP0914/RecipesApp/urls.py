from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='RecipesHome'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('recipe_book/', views.recipe_book, name="recipe_book"),
    path('recipe_api/', views.recipe_api, name='recipe_api'),
    path('recipe_details/<int:pk>/', views.recipe_details, name="recipe_details"),
    path('edit_recipe/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('search/', views.search, name="search"),
    path('nutrition/', views.nutrition, name='nutrition'),
]

