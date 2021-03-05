from django.urls import path
from .import views

FishKeepingApp = 'FishKeepingApp'

urlpatterns = [
    path('', views.home, name='FishKeepingHome'),
    path('create/', views.FishKeeping_CreateUser, name='create'),
    path('wishlist/', views.FishKeeping_WishList, name='wishlist'),
    path('ShowWishList/<int:pk>', views.FishKeeping_ShowWishList, name='ShowWishList'),
    path('details/<int:pk>', views.FishKeeping_Details, name='details'),
]
