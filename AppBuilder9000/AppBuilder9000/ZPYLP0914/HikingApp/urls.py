from django.urls import path
from .import views


urlpatterns = [
    # URL pattern to home page , views function home , named happ_home
    path('', views.home, name='happ_home'),

    # URL pattern to my _profile page , views function create_the_happ_user , named happ_my_profile
    path('my_profile/', views.create_the_happ_user, name='happ_my_profile'),

    # URL pattern to survey page, views function daily_survey , named happ_survey
    path('survey/', views.daily_survey, name='happ_survey'),

    # URL pattern to survey results page , views function survey_result , named survey_result
    path('survey_results/', views.survey_result, name='survey_results'),

    # URL pattern details page , views function details , named survey_results_details
    path('details/<int:pk>', views.details, name='survey_results_details'),

]