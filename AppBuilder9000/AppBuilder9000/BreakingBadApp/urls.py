from django.urls import path
from . import views

urlpatterns = [
    path('', views.breakingbad_home, name='BreakingBadHome'),
    path('addepisode', views.breakingbad_addepisode, name='BreakingBadAddEpisode'),
    path('savedepisodes', views.breakingbad_savedepisodes, name='BreakingBadSavedEpisodes'),
]