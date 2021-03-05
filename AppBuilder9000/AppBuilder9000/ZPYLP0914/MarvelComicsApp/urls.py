from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='MarvelComicsAppHome'),
    path('createsub/', views.subscriber_create_view, name='MarvelComicsAppCreateSubscriber'),
    path('subindex/', views.subscriber_index_view, name='MarvelComicsAppSubscriberIndex'),
    path('subdetails/<int:pk>/', views.subscriber_detail_view, name="MarvelComicsAppSubscriberDetail"),
    path('subedit/<int:pk>/', views.subscriber_edit_view, name='MarvelComicsAppEditSubscriber'),
    path('subdelete/<int:pk>/', views.subscriber_delete_view, name='MarvelComicsAppDeleteSubscriber'),
    path('search/', views.search_view, name='MarvelComicsAppSearch'),
    path('results/<str:data>/', views.results_view, name='MarvelComicsAppResults'),
    path('random/', views.random_view, name='MarvelComicsAppRandom'),
]
