from django.forms import ModelForm
from .models import Climb, Attempt
from django.forms.widgets import *


#-------- CLIMB FORM -----------
class ClimbForm(ModelForm):
    class Meta:
        model = Climb
        fields = '__all__'
        widget = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
            'grade': Select(attrs={'class': 'form-control'}),
            'pitches': TextInput(attrs={'class': 'form-control'}),
            'rock': Select(attrs={'class': 'form-control'}),
            'image': TextInput(attrs={'placeholder': 'optional', 'class': 'form-control', 'type': 'url'})
        }


#-------- ATTEMPT FORM -----------
class AttemptForm(ModelForm):
    class Meta:
        model = Attempt
        fields = '__all__'
        widget = {
            'climb': DateInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'light': Select(attrs={'class': 'form-control'}),
            'temp': TextInput(attrs={'class': 'form-control'}),
            'shoes': TextInput(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
            'notes': TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'})
        }

#TODO Consider adding a tick-list form for adding future climbing projects

#-------- MYSENDS FORM --------