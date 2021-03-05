from django.forms import ModelForm, DateInput, Textarea
from .models import Encounter


class EncounterForm(ModelForm):
    class Meta:
        model = Encounter
        fields = '__all__'
        widgets = {
            'enc_date': DateInput(attrs={'type': 'date'}),
            'description': Textarea()
        }
