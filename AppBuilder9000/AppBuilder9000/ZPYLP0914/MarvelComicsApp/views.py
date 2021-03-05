from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateSubscriber
from .models import Subscriber
from django.core.paginator import Paginator
#For the Marvel Comics API
import requests
from datetime import datetime
from hashlib import md5
import json
import random



def home(request):
    #using the django render function to show the MarvelComicsApp_home.html file
    return render(request, 'MarvelComicsApp/MarvelComicsApp_home.html')

def subscriber_create_view(request):
    #passing the CreateSubscriber form in the 'form' variable only if the form was processed with the post method
    form = CreateSubscriber(request.POST or None)
    #using django's 'is_valid' function to validate form
    if form.is_valid():
        #if the form is valid use django's 'save' function to save the info to the database
        form.save()
        #redirect user to the MarvelComicsHome url
        return redirect('MarvelComicsAppHome')
    return render(request, "MarvelComicsApp/MarvelComicsApp_createsub.html", {'form': form})

def subscriber_index_view(request):
    #grabbing all the information from the Subscriber model manager and passing it into the 'subscribers_list' variable
    subscribers_list = Subscriber.object.all()
    #calling django's built in paginator and passing in the subscribers_list variable which will give all the info from the Subscriber model manager and limiting the list to 5 items per page
    paginator = Paginator(subscribers_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        subscribers = paginator.page(page)
    except(EmptyPage, InvalidPage):
        subscribers = paginator.page(paginator.num_pages)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_index.html', {'subscribers':subscribers})

def subscriber_detail_view(request, pk):
    subscribers = get_object_or_404(Subscriber, pk=pk)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_subdetail.html', {'subscribers':subscribers})

def subscriber_edit_view(request, pk):
    subscribers = get_object_or_404(Subscriber, pk=pk)
    if request.method == 'POST':
        form = CreateSubscriber(request.POST, instance=subscribers)
        if form.is_valid():
            subscribers.save()
            return redirect('MarvelComicsAppSubscriberDetail', pk=subscribers.pk)
    else:
        form = CreateSubscriber(instance=subscribers)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_edit.html', {'form': form})

def subscriber_delete_view(request, pk):
    subscribers = get_object_or_404(Subscriber, pk=pk)
    if request.method == 'POST':
        subscribers.delete()
        return redirect('MarvelComicsAppSubscriberIndex')
    return render(request, 'MarvelComicsApp/MarvelComicsApp_delete.html', {'subscribers':subscribers})

#varibales used for the hash_params function and results_view
timestamp = datetime.now().strftime('%y-%m-%d%H:%M:%S')
pub_key = 'd14caeb1fb2188a04c30c89c3ed44406'
priv_key = '275f19d292e0b0bd391fe9e865183083531a37b5'

#will not be displayed as a view but is needed for the api_view
def hash_params():
    hash_md5 = md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

def search_view(request):
    if request.method == 'POST':
        data = request.POST.get('search')
        return redirect('MarvelComicsAppResults', data)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_search.html')

def results_view(request, data):
    params = {'nameStartsWith': data, 'limit': 3, 'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
    res = requests.get('https://gateway.marvel.com:443/v1/public/characters', params=params)
    results = res.json()
    characters = results['data']['results']
    heros_info = []
    for character in characters:
        images = character['thumbnail']
        characters_info = {'names': character['name'], 'descriptions': character['description'],
                           'paths': images['path'], 'extensions': images['extension']}
        print(characters_info)
        heros_info.append(characters_info)

    return render(request, 'MarvelComicsApp/MarvelComicsApp_results.html', {'heros_info': heros_info})

def random_view(request):
    params = {'limit': 1, 'offset': random.randrange(1, 1500),  'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
    res = requests.get('https://gateway.marvel.com:443/v1/public/characters', params=params)
    results = res.json()
    random_characters = results['data']['results']
    random_heros_info = []
    for random_character in random_characters:
        images = random_character['thumbnail']
        characters_info = {'names': random_character['name'], 'descriptions': random_character['description'],
                           'paths': images['path'], 'extensions': images['extension']}
        print(characters_info)
        random_heros_info.append(characters_info)
    print(random_heros_info)
    return render(request, 'MarvelComicsApp/MarvelComicsApp_random.html', {'random_heros_info': random_heros_info})






