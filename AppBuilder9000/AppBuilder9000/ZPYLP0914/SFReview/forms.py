from django.forms import ModelForm
from .models import BookReview
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = '__all__'
