from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.
def home(request):
    return render(request, 'RealEstateApp/RealEstateApp_index.html')


def client_create(request):
    form = ClientForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('RealEstateHome')
    content = {'form': form}
    return render(request, 'RealEstateApp/RealEstateApp_client_create.html', content)


def client_list(request):
    clients = Client.objects.all()
    # maybe try clients = Client.objects.filter(first_name__icontains='s')
    context = {'clients': clients}
    return render(request, 'RealEstateApp/RealEstateApp_client_list.html', context)


def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    context = {
        'client': client,
    }
    return render(request, 'RealEstateApp/RealEstateApp_details.html', context)

#def favorite(request):
    #form = favorite(data=request.POST or None)
   # if request.method == 'POST':
    #    if form.is_valid():
     #       form.save()
     #       return redirect('RealEstateHome')
  #  content = {'form': form}
   # return render(request, 'RealEstateApp/RealEstateApp_favorite.html', content)


#def bank(request):
   # form = PrimaryBankForm(data=request.POST or None)
   # if request.method == 'POST':
       # if form.is_valid():
           # form.save()
           # return redirect('RealEstateHome')
      #  content = {'form': form}
      #  return render(request, 'RealEstateApp_something.html', content)
