from django.shortcuts import render, redirect, get_object_or_404
from .models import Characters
from .forms import CharacterForm
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
import requests
import json
from bs4 import BeautifulSoup

# Renders home page.
def rickandmorty_home(request):
    return render(request, 'RickAndMorty/RickAndMorty_home.html')

# Saves entries in submitted form to database.
def add_character(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            #print(form)
            #print("Valid Form")
            form.save()
            return redirect('RickAndMorty_home')
        #else:
            #print("Invalid Form")
            #print(form.errors)
    context = {'form': form}
    return render(request, 'RickAndMorty/RickAndMorty_add_character.html', context)

# Submits all entries in database to index page.
def index(request):
    stats = Characters.objects.all()
    return render(request, 'RickAndMorty/RickAndMorty_index.html', {'stats': stats})

# Takes selected entry from index page and returns all values from database
def details(request, pk):
    pk = int(pk)
    character_stats = get_object_or_404(Characters, pk=pk)
    #print(character_stats)
    return render(request, 'RickAndMorty/RickAndMorty_details.html', {'character_stats': character_stats})

# Displays form with current values for selected database entry
# Allows for editing of values
def update(request, pk):
    selected_character = {}
    obj = get_object_or_404(Characters, pk=pk)
    form = CharacterForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('RickAndMorty_details')
    selected_character['form'] = form
    return render(request, 'RickAndMorty/RickAndMorty_update.html', selected_character)

# Renders page to confirm delete, if confirmed entry deleted.
def delete(request,pk):
    delete_character = {}
    obj = get_object_or_404(Characters, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('/RickAndMorty/rick_index')
    return render(request, "RickAndMorty/RickAndMorty_delete.html", delete_character)

# Takes user input and queries API, displaying results on page.
# If no results for that query, display 'oops' page.
def api_search(request):
    character_list = []
    character_data = {}
    if request.method == 'POST':
        results = request.POST.get('character_search', None)
        payload = {'name': results}
        r = requests.get('https://rickandmortyapi.com/api/character/', params=payload)
        if r:
            print(r.url)
            character_data = r.json()
            print(json.dumps(character_data, indent = 1))
            #print(character_data['results'][0]['name'])
            character_results = {
                # pulling the elements of 'name', 'species', 'gender'
                # 'status', 'image', 'origin', and 'location'
                'name': character_data['results'][0]['name'],
                'species': character_data['results'][0]['species'],
                'gender': character_data['results'][0]['gender'],
                'status': character_data['results'][0]['status'],
                'image': character_data['results'][0]['image'],
                'origin': character_data['results'][0]['origin']['name'],
                'location': character_data['results'][0]['location']['name']
            }
            character_list.append(character_results)
            print(character_list)
            context = {"character_list": character_list}
            return render(request, 'RickAndMorty/RickAndMorty_api_search.html', context)

        else:
            return redirect('oops')

    return render(request, 'RickAndMorty/RickAndMorty_api_search.html')

# Renders oops page.
def oops(request):
    return render(request, 'RickAndMorty/RickAndMorty_oops.html')




def bs_search(request):
    total = []
    if request.method == 'POST':
        results = request.POST.get('character_bio')
        print(results)

        if results:
            page = requests.get('https://rickandmorty.fandom.com/wiki/' + results)
            soup = BeautifulSoup(page.content, 'html.parser')
            if results == 'Rick_Sanchez':
                bio1 = soup.find_all('p')[3]
                bio_text1 = bio1.get_text()
                bio2 = soup.find_all('p')[4]
                bio_text2 = bio2.get_text()
                bio3 = soup.find_all('p')[5]
                bio_text3 = bio3.get_text()
            else:
                bio1 = soup.find_all('p')[1]
                bio_text1 = bio1.get_text()
                bio2 = soup.find_all('p')[2]
                bio_text2 = bio2.get_text()
                bio3 = soup.find_all('p')[3]
                bio_text3 = bio3.get_text()

            image = soup.find_all('img')[1]
            image_src = image.get('src')
            print(image_src)
            data_scrape = {
                'bio_text1': bio_text1,
                'bio_text2': bio_text2,
                'bio_text3': bio_text3,
                'image_src': image_src
            }
            print(data_scrape)
            total.append(data_scrape)
            context = {'total': total}
            return render(request, 'RickAndMorty/RickAndMorty_bs.html', context)

    return render(request, 'RickAndMorty/RickAndMorty_bs.html')




