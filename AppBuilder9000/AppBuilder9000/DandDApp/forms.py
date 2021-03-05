from django.forms import ModelForm
from .models import CreateCharacter


class CreateCharacterForm(ModelForm):
    class Meta:
        model = CreateCharacter
        fields = '__all__'
