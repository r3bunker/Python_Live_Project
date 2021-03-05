import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import *
from .models import savecities, cities
import requests

# homepage
def Central_Africa_Republic_home(request):
    return render(request, 'RcanavApp/RcanavApp_home.html')

def thingstodo(request):
    return render(request, 'RcanavApp/RcanavApp_Thingstodo.html')


#save cities
def save_cities(request):
    context = {}
    #create object of form
    form = CitiesForm(request.POST or None)
    #check if form data is valid
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request,'RcanavApp/RcanavApp_save_cities.html', context)

#wishlist
def cities_wish_list_index(request):
    city = savecities.objects.all()
    context = {
        'city_list': city
    }
    return render(request, 'RcanavApp/RcanavApp_wish_index.html', context)

def cities_hotels(request):
    return render(request,'RcanavApp/Rcanav_Hotels.html')

def cities_details(request, pk):
    pk = int(pk)
    city = savecities.objects.get(pk=pk)
    context = {
        'city': city
    }
    return render(request, 'RcanavApp/RcanavApp_details.html', context)

# function for edit
def edit(request, pk):
    pk = int(pk)
    city = savecities.objects.get(pk=pk)
    if request.method == 'POST':
        form = CitiesForm(request.POST, instance=city)
        if form.is_valid():
           city = form.save()
           city.save()
           return redirect('save_cities', pk=city.pk)
    else:
        form = CitiesForm(instance=city)
    context = {'form': form, 'pk':pk}
    return render(request, 'RcanavApp/RcanavApp_edit.html', context)#render to edit template using the context and request

def delete(request, pk):
    pk = int(pk)
    city = savecities.objects.get(pk=pk)
    #if user submits, model instance is deleted
    if request.method == 'POST':
        city.delete()
        return redirect('Thingstodo') #return to things to do page
    context = {'city':city}
    return render(request, "RcanavApp/RcanavApp_delete.html", context)

def api_response(request):
    query = request.GET.get('q') #getting user input
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/" #Api endpoint(string)
    querystring = {"query": query} #creating a dictionnary to pass the user input to the API


    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "a478d8d568msh5e1a59fb6babba5p162906jsndbd8a9e2c4f9"
     }#from the Api it's will be provided
# 75 to 82 is setting up the data to be pass from 84 is requesting the data that been set
    response = requests.request("GET", url, headers=headers, params=querystring)# is packaging all the data that been set from line 75 to 82 that's been set to the Api

    print(response.text)
    result_dict = json.loads(response.text)
    return render(request, "RcanavApp/RcanavaApp_api.html", {"city":result_dict})
    # if query:
    #     get_cities = savecities.cities_name.filter(
    #         Q(cities_icontains=query)).distinct()
    #     paginator = Paginator(get_cities, 10)
    #     page = request.GET.get('page')
    #     try:
    #         cities_page = paginator.page(page)
    #     except PageNotAnInteger:
    #         cities_page = paginator.page(1)
    #     except EmptyPage:
    #         cities_page = paginator.page(paginator.num_pages)
    #     print("inside query")
    #     context = {'save_cit': cities_page,
    #                'get_cities': get_cities
    #                }
    #     return render(request, 'RcanavApp/RcanavaApp_api.html', context)
    # print("outside query")
