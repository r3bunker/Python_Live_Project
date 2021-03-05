from django.shortcuts import render, redirect


# Create your views here.
def StocksTraderHome(request):
    return render(request, 'StocksTraderHome.html',)

def Stocks_Base(request):
    return render(request, 'StocksTraderApp/Stocks_Base.html')
