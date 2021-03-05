from django.contrib import admin
from django.urls import path
from . import views


# the urlpatterns list routes URLs to the views methods.
# To differentiate url names between apps so Django knows
# which app view to create for a url when using the template tag.

urlpatterns = [
    path('', views.surfApp_home, name='SurfSpotsHome'),
    path('AddSpot', views.surfApp_addSpot, name='AddSpot'),
    path('SpotIndex', views.surfApp_index, name='SpotIndex'),
    path('<int:pk>/SpotDetails', views.surfApp_details, name='SpotDetails'),
    path('<int:pk>/UpdateSpot', views.surfApp_update, name='UpdateSpot'),
    path('<int:pk>/DeleteSpot', views.surfApp_delete, name='DeleteSpot'),
    path('<int:pk>/ConfirmDelete', views.confirm_delete, name='ConfirmDelete'),
]
