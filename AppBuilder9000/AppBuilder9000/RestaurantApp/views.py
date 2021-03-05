from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Restaurant
from .forms import RestaurantForm
from bs4 import BeautifulSoup
import requests

#zomato api key
auth = {'user-key': 'e3491d1b716b19e9800329944dce6985'}
#here map api key is found in the javascript in search.html (bottom of page)


#home page
def Restaurant_home(request):
    return render(request, 'RestaurantApp/RestaurantApp_home.html')


#MyList: index of restaurants - show.html
def Restaurant_show(request):
    restaurants = Restaurant.objects.all()
    content = {'restaurants': restaurants,}
    return render(request, 'RestaurantApp/RestaurantApp_show.html', content)


#details page
def Restaurant_details(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    content = {'restaurant': restaurant}
    return render(request, 'RestaurantApp/RestaurantApp_details.html', content)


#edit page
def Restaurant_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            restaurant.save()
            messages.success(request, "Your changes were saved!")
            return redirect('RestaurantShow')
        else:                       #this should be nearly impossible to trigger, however it still exists
            messages.error(request, "Please make sure all fields are valid")
            print(form.errors)
            return redirect('RestaurantEdit', pk)
    else:
        form = RestaurantForm(instance=restaurant)
    content = {'form': form, 'pk': pk, 'restaurant': restaurant,}
    return render(request, 'RestaurantApp/RestaurantApp_edit.html', content)


#add restaurant
def Restaurant_add(request):
    form = RestaurantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your restaurant was added to MyList")
            return redirect('RestaurantShow')
        else:                   # this should be nearly impossible to trigger, however it still exists
            messages.error(request, "Please make sure all fields are valid")
            return redirect('RestaurantAdd')
    content = {'form': form,}
    return render(request, 'RestaurantApp/RestaurantApp_add.html', content)


#delete function for show, details, and edit pages
def Restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        restaurant.delete()
        return redirect('RestaurantShow')
    return redirect('RestaurantShow')


#save to MyList feature in search.html
def Restaurant_save(request):
    form = RestaurantForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            newform = form.save(commit=False)
            newform.establishment = str(newform.establishment)[1:-1].strip("'")     #establishment is always given in a list
            newform.save()                                  #   this removes the brackets and quotes so we can save just the
            print(newform.establishment)                    #   string values to the database (otherwise brackets show up on show.html)
            return redirect('RestaurantShow')
    else:                               #if the user tries to access through URL, we're sending them back to homepage
        return redirect('RestaurantHome')


#search by city on home page, this is a two-step process, we first need to query zomato for city id (multiple cities exist with the same name)
def Restaurant_api(request):
    if request.method == 'POST':
        city = request.POST.get('userCity')     #grab user input
        response = requests.get('https://developers.zomato.com/api/v2.1/cities?q={}'.format(city), headers=auth)
        city_data = response.json()["location_suggestions"]
        if city_data == []:                     #if the response came back empty
            messages.error(request, "Your city didn't match any in our database - try one more time!")
            return redirect('RestaurantHome')   #sends ^this alert message and keeps user on home page
        else:                                   #otherwise if the response has data in it
            cities = {}                         #new dictionary to store incoming data
            i = 0
            while i < len(city_data):           #cycle through all of the returned data and only display
                id = city_data[i]["id"]         #   city names and their corresponding id which we will need
                name = city_data[i]["name"]     #   to query the api again
                cities.update({id: name})       #actually appends, rather than update, so existing entries are not overwritten
                i += 1

            content = {
                'go': True,                     #this triggers the jQuery to open the "did you mean" modal
                'cities': cities,               #carries our new dictionary into modal
            }
            return render(request, 'RestaurantApp/RestaurantApp_home.html', content)


#search result from user input, only runs after user selects specific city
def Restaurant_search(request, key):
    id = key                                #key is specified by which city the user selects
    locresponse = requests.get('https://developers.zomato.com/api/v2.1/location_details?entity_id={}&entity_type=city'.format(id), headers=auth)
    lat = locresponse.json()["location"]["latitude"]            #accessing zomato api for city's latitude and longitude
    lon = locresponse.json()["location"]["longitude"]           #   needed for filtering
    response = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id={}&entity_type=city'.format(id), headers=auth)
    content = iterateResponse(response, lat, lon)                #function located lower down
    return render(request, 'RestaurantApp/RestaurantApp_search.html', content)


#search near me button, functions exactly like restaurant_search except utilizes user's geolocation
def Restaurant_nearme(request):
    locresponse = requests.get('http://ip-api.com/json/')       #geolocation api, assumes user's IP, is a rough guess - not completely accurate
    lat = locresponse.json()['lat']
    lon = locresponse.json()['lon']
    response = requests.get('https://developers.zomato.com/api/v2.1/search?lat={}&lon={}'.format(lat, lon), headers=auth)
    content = iterateResponse(response, lat, lon)
    return render(request, 'RestaurantApp/RestaurantApp_search.html', content)


#filtering search results, this is should only be available after user has established city they're searching
def Restaurant_filter(request):
    lat = request.POST.get('currentlat')                   #keeping track of the city we're searching/filtering
    lon = request.POST.get('currentlon')
    if request.method == 'POST':                    #if user accessed the page through url, this will deny them
        q = request.POST.get('q')                   #search box
        rawradius = request.POST.get('radius')
        zradius = int(rawradius)*1000               #make sure it's an integer, not binary
        radius = int(zradius)                       #probably no decimals, but safety first
        sortby = request.POST.get('sortby')
        if sortby == 'ratingHtoL' or 'blank':       #transforming sort by into values we can
            sort = 'rating'                         #   query the api with
            order = 'desc'                          # 'or "blank"' meaning - if the user didn't specify, we'll deliver
        if sortby == 'ratingLtoH':                  #   the results as best rating to worst rating
            sort = 'rating'
            order = 'asc'
        if sortby == 'priceHtoL':
            sort = 'cost'
            order = 'desc'
        if sortby == 'priceLtoH':
            sort = 'cost'
            order = 'asc'
        response = requests.get('https://developers.zomato.com/api/v2.1/search?q={}&lat={}&lon={}&radius={}&sort={}&order={}'.format(q, lat, lon, radius, sort, order), headers=auth)
        content = iterateResponse(response, lat, lon)
        return render(request, 'RestaurantApp/RestaurantApp_search.html', content)
    else:
        return redirect('RestaurantNearMe')         #if user tried to navigate to /search/filter through url, we're bumping them to nearme function instead


def iterateResponse(response, lat, lon):
    #each function's response variable queries the api a little bit differently, this is where they all catch up the same;
    city_data = response.json()["restaurants"]
    restaurants = {}                                                        #setting up dictionary to store all our needed data
    i = 0
    while i < len(city_data):                                               #cycle through each restaurant we received from api
        id = city_data[i]["restaurant"]["id"]                               #this is all the data we are requesting from the api each time
        name = city_data[i]["restaurant"]["name"]
        url = city_data[i]["restaurant"]["url"]
        img = city_data[i]["restaurant"]["thumb"]
        address = city_data[i]["restaurant"]["location"]["address"]
        latitude = city_data[i]["restaurant"]["location"]["latitude"]
        longitude = city_data[i]["restaurant"]["location"]["longitude"]
        cuisines = city_data[i]["restaurant"]["cuisines"]
        hours = city_data[i]["restaurant"]["timings"]
        avgfortwo = city_data[i]["restaurant"]["average_cost_for_two"]
        pricerange = city_data[i]["restaurant"]["price_range"]
        highlights = city_data[i]["restaurant"]["highlights"]
        rating = city_data[i]["restaurant"]["user_rating"]["aggregate_rating"]
        rating_text = city_data[i]["restaurant"]["user_rating"]["rating_text"]
        votes = city_data[i]["restaurant"]["user_rating"]["votes"]
        menu = city_data[i]["restaurant"]["menu_url"]
        phone = city_data[i]["restaurant"]["phone_numbers"]
        establishment = city_data[i]["restaurant"]["establishment"]
        if img == '':              #if the api returned nothing for img
            try:
                useragent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
                shortURL = url.split('?')[0]                                                       #(^user agent is needed to gain access)
                page = requests.get(shortURL + '{}'.format('?amp=1'), headers=useragent, allow_redirects=False)
                soup = BeautifulSoup(page.content, 'html.parser')           #use beautiful soup to data scrape the site with the
                try:                                                        #    url we already have and add an image
                    src = soup.findAll('amp-img')[1]['src']
                    img = src.split('?')[0]                                 #this split is just to clean the jpg of any filters/cropping
                except:
                    src = soup.findAll('amp-img')[2]['src']
                    img = src.split('?')[0]
            except :
                pass
        restaurants.update({i: {
            'id': id, 'name': name, 'url': url, 'img': img, 'address': address, 'latitude': latitude,
            'longitude': longitude, 'cuisines': cuisines, 'hours': hours, 'avgfortwo': avgfortwo,
            'pricerange': pricerange, 'highlights': highlights, 'rating': rating, 'rating_text': rating_text,
            'votes': votes, 'menu': menu, 'phone': phone, 'establishment': establishment,
        }})
        i += 1
    cityresponse = requests.get('https://developers.zomato.com/api/v2.1/cities?lat={}&lon={}'.format(lat, lon), headers=auth)
    city = cityresponse.json()['location_suggestions'][0]['name']              #this is to be able to display the city name at the top of the page
    content = {'restaurants': restaurants, 'city': city, 'lat': lat, 'lon': lon,}
    return content

