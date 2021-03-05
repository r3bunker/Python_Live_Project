from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="RealEstateHome"),
    path('clients/', views.client_list, name="client_list"),
    path('clients/<pk>/', views.client_detail, name="client_detail"),

    # CRUD
    path('clients/create-client', views.client_create, name="client_create"),
]
