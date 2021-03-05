from django.forms import ModelForm, DateInput
from .models import savecities
from django import forms
#
# # creating from for save cities
class DateInput(forms.DateInput):
 input_type = 'date'

class CitiesForm(ModelForm):
    class Meta:
        model = savecities
        fields = '__all__'
        widgets = {
            'date_saved': DateInput()
        }