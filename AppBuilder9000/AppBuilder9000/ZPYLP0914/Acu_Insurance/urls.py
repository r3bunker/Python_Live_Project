from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Acu_Insurance'),
    path('index', views.index, name='index'),
    path('add', views.add, name='add'),
    path('addInsurance', views.addInsurance, name='addInsurance'),
    path('Thanks', views.thanks, name='Thanks'),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),
]
