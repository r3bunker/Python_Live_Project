from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CreateCharacterForm
from .models import CreateCharacter
from django.views.generic.list import ListView
from django.core.paginator import Paginator


def d_and_d_home(request):
    return render(request, 'DandDApp/DandD_home.html')


def add_character(request):
    form = CreateCharacterForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('DandDHome')
    else:
        print(form.errors)
        form = CreateCharacterForm()
    context = {'form': form}
    return render(request, 'DandDApp/Add_Character.html', context)


def d_and_d_index(request):
    form = CreateCharacterForm()
    characters = CreateCharacter.object.all()
    paginator = Paginator(characters, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'form': form, 'characters': characters}
    return render(request, 'DandDApp/DandD_index.html', {'page_obj': page_obj}, context)


def d_and_d_details(request, pk):
    character = get_object_or_404(CreateCharacter, pk=pk)
    context = {'character': character}
    return render(request, 'DandDApp/DandD_Details.html', context)


