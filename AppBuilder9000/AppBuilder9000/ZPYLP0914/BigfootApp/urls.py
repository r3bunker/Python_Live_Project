from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bigfoot_home, name='BigfootHome'),
    path('new_encounter/', views.new_encounter, name='new_encounter'),
    path('encounter_index/', views.encounter_index, name='encounter_index'),
    path('<int:pk>/details/', views.encounter_details, name='encounter_details'),
    path('<int:pk>/edit/', views.encounter_edit, name='encounter_edit'),
    path('<int:pk>/delete/', views.encounter_delete, name='encounter_delete'),
    path('submission', views.submission, name='submission'),
    path('report_deleted', views.report_deleted, name='report_deleted'),
    path('report_edited', views.report_edited, name='report_edited'),
]
