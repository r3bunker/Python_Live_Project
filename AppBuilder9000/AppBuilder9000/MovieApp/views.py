from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import User, Movie
from .forms import CreateProfile
# Create your views here.


def home(request):
    return render(request, 'MovieApp/movieapp_home.html')


def create_profile(request):
    form = CreateProfile(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MovieAppHome')
    context = {'form': form}
    return render(request, 'MovieApp/create_profile.html', context)


def movieapp_index(request):
    user = User.Users.all()
    context = {'user': user}
    return render(request, 'MovieApp/movieapp_index.html', context)


def movieapp_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {'user': user}
    return render(request, 'MovieApp/movieapp_details.html', context)