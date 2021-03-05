from django.shortcuts import render, redirect
from .models import Cocktail
from .forms import CocktailForm


def Cocktail_home(request):
    return render(request, 'CocktailRecipesApp/CocktailRecipes_Home.html')


def Cocktail_create(request):
    form = CocktailForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CocktailRecipesAll')
    content = {'form': form}
    return render(request, 'CocktailRecipesApp/CocktailRecipes_Create.html', content)


def Cocktail_all(request):
    cocktail = Cocktail.objects.all()
    content = {'list_of_cocktails': cocktail}
    return render(request, 'CocktailRecipesApp/CocktailRecipes_All.html', content)


def Cocktail_details(request, pk):
    cocktail = Cocktail.objects.get(pk=pk)
    content = {'cocktail': cocktail}
    return render(request, 'CocktailRecipesApp/CocktailRecipes_Details.html', content)
