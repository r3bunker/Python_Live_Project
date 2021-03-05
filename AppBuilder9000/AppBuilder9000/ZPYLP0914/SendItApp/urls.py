from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendit_home, name='SendItHome'),
    path('create/', views.create, name='Create'),
    path('climb_create/', views.climb_create, name='ClimbCreate'),
    path('attempt_create/', views.attempt_create, name='AttemptCreate'),
    path('my_sends/', views.my_sends, name='MySends'),
    path('climb_detail/<int:pk>/', views.climb_detail, name='ClimbDetail'),
    path('attempt_detail/<int:pk>/', views.attempt_detail, name='AttemptDetail'),
    path('climb_edit/<int:pk>/', views.climb_edit, name='ClimbEdit'),
    path('attempt_edit/<int:pk>/', views.attempt_edit, name='AttemptEdit'),
    path('climb_delete/<int:pk>/', views.climb_delete, name='ClimbDelete'),
    path('attempt_delete/<int:pk>/', views.attempt_delete, name='AttemptDelete'),
]
