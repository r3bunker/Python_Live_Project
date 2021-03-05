from django.urls import path
from .import views

urlpatterns =[
    path('', views.approach_home, name='ApproachHome'),
    path('SignIn/CreateUser/', views.create_user, name='CreateUser'),
    path('SignIn/', views.sign_in, name='SignIn'),
    path('TickList/', views.tick_list, name='TickList'),
    path('TickList/AddClimb', views.add_climb, name='AddClimb'),
    path('TickList/<int:pk>/details', views.view_climb, name='ViewClimb'),
    path('TripManager/', views.trip_manager, name='TripManager'),
    path('TripManager/NewTrip', views.new_trip, name='NewTrip'),
    path('TripManager/<int:pk>/details', views.view_trip, name='TripViewer'),
    path('Guidebooks/', views.guidebooks, name='GuideBooks'),
    path('Guidebooks/AddGuidebook', views.addguidebook, name='AddGuidebook'),
    path('Guidebooks/<int:pk>/details', views.view_guidebook, name='ViewGuidebook'),
    path('Training/', views.training, name='Training'),

]
