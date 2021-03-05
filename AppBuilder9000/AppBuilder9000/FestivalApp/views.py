from django.shortcuts import render, redirect, get_object_or_404
from .models import FestivalReview, USCities
from .forms import ReviewForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json
import os
from django.contrib import messages
from django.http import HttpResponse
from bs4 import BeautifulSoup

# Create your views here.
def festival_home(request):
    return render(request, 'FestivalApp/FestivalApp_home.html')

def create_review(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print("Valid Form")
            form.save()
            messages.success(request, 'Review successfully submitted.')
            return redirect('FestivalApp:create_review')
        else:
            print("Invalid Form")
            print(form.errors)
    context = {'form': form}
    return render(request, 'FestivalApp/FestivalApp_create_review.html', context)

def reviews_index(request):
    get_reviews = FestivalReview.reviews.all()
    # print(len(get_reviews))
    # The query variable grabs the string item 'q' from the db based on the search input field in reviews_index page.
    query = request.GET.get('q')
    if query:
        get_reviews = FestivalReview.reviews.filter(
            Q(review_date__icontains=query) | Q(festival_title__icontains=query) | Q(rating__icontains=query)
        ).distinct()
    # else:
    #     messages.error(request, 'Sorry, no reviews for that. Try searching something else.')

    paginator = Paginator(get_reviews, 10)
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    context = {'FestivalReview_list': reviews,
               'get_reviews': get_reviews
               }
    return render(request, 'FestivalApp/FestivalApp_reviews_index.html', context)

def review_details(request, id):
    selected_review = get_object_or_404(FestivalReview, pk=id)
    context = {'selected_review': selected_review}
    return render(request, 'FestivalApp/FestivalApp_review_details.html', context)

def edit_review(request, id):
    review = get_object_or_404(FestivalReview, pk=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            # The 'id' argument will be passed to the above 'review_details' function.
            return redirect('FestivalApp:review_details', id=review.id)
    else:
        form = ReviewForm(instance=review)
        context = {'form': form}
        return render(request, 'FestivalApp/FestivalApp_edit_review.html', context)

def delete(request, id):
    review = get_object_or_404(FestivalReview, pk=id)
    if request.method == 'POST':
        review.delete()
        return redirect('FestivalApp:reviews_index')
    else:
        return redirect('FestivalApp:review_details')

def festivals_bs(request):
    page = requests.get('https://visitseattle.org/events/?frm=events&s=')
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    results = soup.find(class_="search-result-container")
    # print(results)
    # print(type(results))
    result_items = results.find_all(class_="search-result")
    festivals_list = []
    for i in result_items:
        # print("========================")
        a_tag = i.find(class_="event-title")
        title = a_tag.text
        # print(title)
        details = []
        p_tags = i.find_all("p")
        for p in p_tags:
            txt = p.text
            details.append(txt)
        # print(details)
        links = []
        for h in i.find_all("a"):
            link = h.get('href')
            links.append(link)
        print(links)

        festivals = {
            "title": title,
            "venue": details[0],
            "dates": details[1],
            "details": links[1],
            "website": links[2]
        }
        # print(festivals)
        festivals_list.append(festivals)
    print(festivals_list)

    context = {"festivals_list": festivals_list}
    return render(request, 'FestivalApp/FestivalApp_festivals_bs.html', context)

# Weather API page
def weather_api(request):
    seed_cities_database()
    query = request.GET.get('q')
    if query:
        get_city = USCities.cities.filter(
            Q(city__icontains=query) |  Q(state__icontains=query)
        ).distinct()

        paginator = Paginator(get_city, 10)
        page = request.GET.get('page')
        try:
            city_page = paginator.page(page)
        except PageNotAnInteger:
            city_page = paginator.page(1)
        except EmptyPage:
            city_page = paginator.page(paginator.num_pages)
        print("inside query")

        context = {'city_list': city_page,
                   'get_city': get_city
                   }
        return render(request, 'FestivalApp/FestivalApp_weather_api.html', context)
    print("outside query")

    seattle = seattle_weather_api()

    context = {'weather_desc': seattle['weather_desc'],
               'feels_like_in_Fahrenheit': seattle['feels_like_in_Fahrenheit'],
               }
    # jprint(weather_desc)
    # jprint(feels_like_in_Fahrenheit)
    return render(request, 'FestivalApp/FestivalApp_weather_api.html', context)

def seed_cities_database():
    with open("FestivalApp/usa_cities.json") as f:
        cities_json = json.load(f)
    # print(len(USCities.cities.all()))
    if len(USCities.cities.all()) < 1:
        i = 0
        while (i < len(cities_json)):
            us_cities = USCities(
                city= cities_json[i]['city'],
                lat= cities_json[i]['lat'],
                lng= cities_json[i]['lng'],
                country= cities_json[i]['country'],
                state= cities_json[i]['state'],
                state_code = cities_json[i]['state_code']
            )
            us_cities.save()
            i += 1

def seattle_weather_api():
    # Seattle API call
    # This call to the api will appear on the page at all times, rendering dynamically.
    api = 'https://api.openweathermap.org/data/2.5/weather'
    city_name = 'Seattle'
    country = 'us'
    weather_city_name = city_name + ',' + country
    api_key = '69b5210e5ff559e06318bbd567995023'
    weather_URI = api + '?q=' + weather_city_name + '&appid=' + api_key
    response = requests.get(weather_URI)

    # print(response.status_code)
    json_response = response.json()
    # print(json_response)
    # jprint(json_response)
    # extracting the name key/value pair from the JSON object.
    # name = response.json()['name']
    weather = json_response['weather']
    weather_desc = weather[0]['description']

    main = json_response['main']
    feels_like_in_Kelvin = main['feels_like']
    feels_like_in_Fahrenheit = round((feels_like_in_Kelvin - 273.15) * 9 / 5 + 32)

    return {'weather_desc': weather_desc, 'feels_like_in_Fahrenheit': feels_like_in_Fahrenheit}

# method to print a formatted string as the JSON output, for readability.
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# def city_index(request, id):


def city_index(request, city, state):
    api = 'https://api.openweathermap.org/data/2.5/weather'
    city_name = city
    state_code = state
    print(state)
    country = 'us'
    weather_city_name = city_name + ',' + state_code + ',' + country
    api_key = '69b5210e5ff559e06318bbd567995023'
    weather_URI = api + '?q=' + weather_city_name + '&appid=' + api_key
    response = requests.get(weather_URI)
    json_response = response.json()
    print(json_response)

    weather = json_response['weather']
    city_weather = weather[0]['description']

    main = json_response['main']
    city_temp_Kelvin = main['feels_like']
    city_temp_Fahrenheit = round((city_temp_Kelvin - 273.15) * 9 / 5 + 32)

    context = {'city_name': city_name,
               'state_code': state_code,
               'city_weather': city_weather,
               'city_temp_Fahrenheit': city_temp_Fahrenheit,
               }
    return render(request, 'FestivalApp/FestivalApp_weather_api.html', context)







