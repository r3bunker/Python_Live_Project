from django.urls import path
from . import views
urlpatterns = [
    path('', views.Movie_home, name="MovieUpHome"),
    path('createItem', views.createItem, name="createItem")

]
