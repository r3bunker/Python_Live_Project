from django.urls import include, path

from . import views


"""-submitted function allows user to see the contents submitted in the database.
   -reviews function allows user to submit a review and input the information """
urlpatterns = [
    path('', views.index, name='index'),
    path('Reviews', views.Reviews, name='Reviews'),
    path('Submitted', views.Submitted, name='Submitted'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]