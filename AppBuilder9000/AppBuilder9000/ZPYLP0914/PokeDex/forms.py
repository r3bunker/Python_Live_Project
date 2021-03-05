from django.forms import ModelForm, Textarea, DateInput
from .models import sighting


class Createsighting(ModelForm):
    class Meta:
        model = sighting
        fields = '__all__'
        widgets = {
            'Pokemon_notes': Textarea(),
            'Pokemon_Date': DateInput(attrs={'type': 'date'})
        }