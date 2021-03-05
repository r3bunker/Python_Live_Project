from django import forms
from django.forms import ModelForm
from .models import FishKeepingUser, FishWishList


class CreateUserForm(ModelForm):
    class Meta:
        model = FishKeepingUser
        fields = '__all__'


class CreateWishListForm(ModelForm):
    class Meta:
        model = FishWishList
        image = forms.URLField(widget=forms.ClearableFileInput)
        fields = '__all__'
