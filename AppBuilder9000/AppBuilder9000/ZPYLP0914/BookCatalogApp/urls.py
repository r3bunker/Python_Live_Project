from django.urls import path
from . import views

# the urlpatterns list routes URLs to the views methods.
# To differentiate url names between apps so Django knows which app view to create for a url when using the
# template tag, add an app_name to set the app namespace.

app_name = 'BookCatalogApp'

urlpatterns = (
    path('', views.book_home, name="book_home"),
    path('create_record', views.CreateView, name='create_record'),
    path('list_index', views.Retrieve_ListView, name='list_index'),
    path('list_detail/<int:id>', views.Retrieve_DetailView, name='list_detail'),
    # path('list_index/<int:_id>/delete', views.DeleteView),
)
