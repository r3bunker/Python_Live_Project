from django.forms import ModelForm
from .models import Star
from .models import Planet
from .models import Moon

class StarForm(ModelForm):
    class Meta:
        model = Star
        fields = '__all__'

class PlanetForm(ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'

class MoonForm(ModelForm):
    class Meta:
        model = Moon
        fields = '__all__'