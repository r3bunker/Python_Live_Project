from django import forms
from .models import Recipe
from django.conf import settings
import requests


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"


class IngredientForm(forms.Form):  # names the form function
    ingredients = forms.CharField(max_length=100)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30)
