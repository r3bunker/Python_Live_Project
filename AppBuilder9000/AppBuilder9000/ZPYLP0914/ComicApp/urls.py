from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ComicHome'),
    path('signup/', views.signup, name='ComicSignUp'),
    path('review/', views.review, name='ComicReview'),
    path('review-index/', views.review_index, name='ComicReviewIndex'),
    path('review-index/<int:review_id>/', views.review_details, name='ComicReviewDetails'),
    path('review-index/edit/<int:review_id>/', views.review_edit, name='ComicReviewEdit'),
    path('review-index/delete/<int:review_id>/', views.review_delete, name='ComicReviewDelete')
]
