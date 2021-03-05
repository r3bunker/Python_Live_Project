from django.forms import ModelForm
from django import forms
from .models import Acu
from .models import Insurance


class AcuForm(ModelForm):
    class Meta:
        model = Acu
        fields = '__all__'


class InsuranceForm(ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'


# widgets go here, can put classes here

