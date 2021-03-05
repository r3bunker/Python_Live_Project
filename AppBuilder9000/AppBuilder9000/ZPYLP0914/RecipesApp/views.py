from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .form import RecipeForm, IngredientForm, SearchForm
from .models import Recipe
import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, "RecipesApp/RecipesApp_home.html")


def new_recipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recipe_book')
    else:
        print(form.errors)
        form = RecipeForm()
    context = {'form': form}
    return render(request, "RecipesApp/RecipesApp_newRecipe.html", context)


def recipe_book(request):
    recipe = Recipe.object.all()  # get recipe model
    page = request.GET.get('page', 1)  # assign recipe page numbers
    paginator = Paginator(recipe, 5)  # assign 5 recipes per page
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
    return render(request, "RecipesApp/RecipesApp_recipe_book.html", {'recipes': recipes})


def recipe_details(request, pk):
    recipe = Recipe.object.get(pk=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'RecipesApp/RecipesApp_recipe_details.html', context)


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_details', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "RecipesApp/RecipesApp_edit.html", {'form': form})


# delete view for details page
def delete_recipe(request, pk):
    # get object related to details pk
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":  # delete object if matches details pk
        recipe.delete()
        # redirect to recipe book page after delete
        return HttpResponseRedirect('/RecipesApp')
    return render(request, 'RecipesApp/RecipesApp_delete_recipe.html', {'recipe': recipe})


def recipe_api(request):
    recipes = {}
    form = IngredientForm(request.GET)
    if 'ingredients' in request.GET:
        i = request.GET['ingredients']
        print(i, "coming from views.py")
        url = 'http://www.recipepuppy.com/api/?i={}'.format(i)
        print(url)
        response = requests.get(url)
        recipes = response.json()
        print(recipes)
    return render(request, 'RecipesApp/RecipesApp_api.html', {'form': form, 'recipes': recipes})


def nutrition(request):  # this creates a view for my nutrition page
    # get the havard webpage on nutrition
    page = requests.get("https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/")
    # parse through html to get info i need
    soup = BeautifulSoup(page.content, 'html.parser')
    # finds the class I want from the html page (harvard's)
    plate = soup.find(class_='entry-content')
    # gets the paragraphs and hrefs from the page
    plate_def = plate.find_all('p')
    plate_link = plate.find_all('a')
    link = []  # empty list to fill with href
    for links in plate_link:
        link.append('{}'.format(links.get('href')))  # adds hrefs to list
    # 2 dictionaries for storing the data i need to display
    links = {"veggies": link[1],
             "grains": link[2],
             "protein": link[6],
             "fats": link[9],
             "drinks": link[11],
             }
    paragraph = {"veggies": plate_def[2].get_text(),
                 "grains": plate_def[3].get_text(),
                 "protein": plate_def[4].get_text(),
                 "fats": plate_def[5].get_text(),
                 "drinks": plate_def[6].get_text(),
                 }
    # renders my page with the two dictionaries
    return render(request, 'RecipesApp/RecipesApp_nutrition.html', {'paragraph': paragraph, "links": links})


def search(request):
    query = request.GET.get('q')
    results = Recipe.object.filter(Title__icontains=query)
    return render(request, "RecipesApp/RecipesApp_search_results.html", {'results': results})
