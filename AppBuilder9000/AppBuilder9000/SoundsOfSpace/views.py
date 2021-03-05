from django.shortcuts import render, redirect, get_object_or_404
from .models import Star, Planet, Moon
from .forms import StarForm, PlanetForm, MoonForm
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect


def SOS_home(request):
    return render(request, 'SOS_home/SOS_home.html')

def add_star(request):
    form = StarForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SoundsOfSpace')
    context = {'form': form}
    return render(request, 'SOS_Home/add_star.html', context)


def add_planet(request):
    form = PlanetForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SoundsOfSpace')
    context = {'form': form}
    return render(request, 'SOS_home/add_planet.html', context)

def add_moon(request):
    form = MoonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SoundsOfSpace')
    context = {'form': form}
    return render(request, 'SOS_home/add_moon.html', context)

def PlanetIndexPage(request):
    form = PlanetForm()
    planet = Planet.planets.all()
    context = {'form': form, 'planet': planet}
    return render(request, 'SOS_home/SOS_PlanetIndex.html', context)

def PlanetDetailPage(request, id):
    planet = Planet.planets.get(pk=id)
    context = {'planet': planet}
    return render(request, 'SOS_home/SOS_PlanetDetail.html', context)







