from django.forms import ModelForm
from .models import PlayerProfile


# Creates player form
class PlayerForm(ModelForm):
    class Meta:
        model = PlayerProfile
        fields = '__all__'
