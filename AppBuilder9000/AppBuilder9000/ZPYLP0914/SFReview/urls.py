from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='SFReview'),                                              #URL for Home page
    path('Create', views.sfr_createreview, name='CreateReview'),                        #Create Reviews page
    path('CreateConfirmed', views.sfr_createconf, name='CreateConfirmed'),                        #Confirmation of Review Creation
    path('Previous/', views.sfr_previousreview, name='PreviousReview'),                 #Previous reviews/details in database page.
    path('Previous/<int:pk>/details/', views.sfr_details, name='details'),              #int:pk identifier for specific reviews.
    path('Previous/<int:pk>/edit/', views.sfr_edit, name='edit'),                       #int:pk to edit the review.
    path('Previous/<int:pk>/remove/', views.sfr_delete, name='remove'),                 #int:pk for specific review to delete.
    path('RemoveConfirmed', views.sfr_delconf, name='RemoveConfirmed'),                 #int:pk confirmation of delete.
    path('Recommendations', views.sfr_goodreads, name='Recommendations'),               #Beautiful soup scrap page.
]
