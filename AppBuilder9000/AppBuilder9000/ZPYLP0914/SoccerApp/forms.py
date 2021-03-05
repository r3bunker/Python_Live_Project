from django.forms import ModelForm
from .models import player

class PlayerForm(ModelForm):
    class Meta:
        model = player
        fields = ['Name', 'Position', 'Team', 'Salary']