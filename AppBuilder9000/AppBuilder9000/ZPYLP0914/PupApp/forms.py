from django.forms import ModelForm
from .models import PlayTime
from .models import Owner

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class PlayTimeForm(ModelForm):
    class Meta:
        model = PlayTime
        fields = '__all__'