from django.forms import ModelForm
from .models import Characters

class CharacterForm(ModelForm):
    class Meta:
        model = Characters
        fields = ['name', 'alignment', 'catchPhrase', 'image', 'description']

