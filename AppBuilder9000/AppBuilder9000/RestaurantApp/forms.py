from django.forms import ModelForm, CheckboxInput, RadioSelect
from .models import Restaurant


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'