from django.forms import ModelForm, TextInput
from .models import User, Movie
from django import forms


class CreateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {'first_name': TextInput(attrs={'class': 'form-control'}),
                   'last_name': TextInput(attrs={'class': 'form-control'}),
                   'password': TextInput(attrs={'class': 'form-control'}),
                   'email': TextInput(attrs={'class': 'form-control'})}


class MovieList(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

