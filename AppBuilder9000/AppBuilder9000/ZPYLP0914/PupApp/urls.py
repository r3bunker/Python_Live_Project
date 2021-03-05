from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='PupHome'),
    path('AddPup/', views.add_pup, name='createPup'), #page to add pup to database
    path('AddOwner', views.add_owner, name='createOwner'),
    path('index', views.index, name='indexPup'), #displays data in database\
    path('<int:pk>/pupapp_details', views.pupapp_details, name='pupDetails'),
    path('<int:pk>/pupapp_edit', views.pupapp_edit, name='pupEdit'),
    path('<int:pk>/pupapp_delete', views.pupapp_delete, name='pupDelete'),
    path('confirmdelete', views.confirmed, name="confirmed"),
]