from django.urls import path
# the '.' states that we will import a file within this same directory, in the 'FestivalApp' directory.
from . import views

# the urlpatterns list routes URLs to the views methods.
# To differentiate url names between apps so Django knows which app view to create for a url when using the
# template tag, add an app_name to set the app namespace.
app_name = 'FestivalApp'
urlpatterns = [
    path('', views.festival_home, name='festival_home'),
    path('create_review', views.create_review, name='create_review'),
    path('reviews_index/', views.reviews_index, name='reviews_index'),
    path('reviews_index/<int:id>/review_details/', views.review_details, name='review_details'),
    path('review_details/<int:id>/edit_review/', views.edit_review, name='edit_review'),
    path('review_details/<int:id>/delete/', views.delete, name='delete'),
    path('weather_api/', views.weather_api, name='weather_api'),
    path('weather_api/<str:city>/<str:state>/city_index/', views.city_index, name='city_index'),
    path('review_details/<int:id>/delete/', views.delete, name='delete'),
    path('festivals_bs', views.festivals_bs, name='festivals_bs'),
]