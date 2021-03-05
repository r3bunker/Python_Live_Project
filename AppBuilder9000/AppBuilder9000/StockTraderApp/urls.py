from django.urls import path
from .import views


urlpatterns = [
    path('', views.StocksTraderHome, name='StocksTraderHome'),
    path('Stocks_Base.html', views.Stocks_Base, name="about"),
]