from django.forms import ModelForm
from .models import SurfSpot

class SurfSpotForm(ModelForm):
    class Meta:
        model = SurfSpot
        fields = '__all__'
