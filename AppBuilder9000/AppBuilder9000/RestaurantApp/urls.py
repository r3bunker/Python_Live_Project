from django.urls import path
from . import views

urlpatterns = [
    path('', views.Restaurant_home, name='RestaurantHome'),
    path('add', views.Restaurant_add, name='RestaurantAdd'),
    path('MyList', views.Restaurant_show, name='RestaurantShow'),
    path('MyList/<int:pk>/delete', views.Restaurant_delete, name='RestaurantMyListDelete'),
    path('details/<int:pk>', views.Restaurant_details, name='RestaurantDetails'),
    path('details/<int:pk>/delete', views.Restaurant_delete, name='RestaurantDetailsDelete'),
    path('details/edit/<int:pk>', views.Restaurant_edit, name='RestaurantEdit'),
    path('details/edit/<int:pk>/delete', views.Restaurant_delete, name='RestaurantEditDelete'),
    path('api', views.Restaurant_api, name='RestaurantApi'),
    path('search/<int:key>', views.Restaurant_search, name='RestaurantSearch'),
    path('search/', views.Restaurant_nearme, name='RestaurantNearMe'),
    path('search/filter', views.Restaurant_filter, name='RestaurantFilter'),
    path('search/save', views.Restaurant_save, name='RestaurantSave'),
]