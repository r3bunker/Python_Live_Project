from django.forms import ModelForm, RadioSelect
from .models import TheBigOne
from .models import TheContact


class TheBigOneForm(ModelForm):
    class Meta:
        model = TheBigOne
        fields = '__all__'
        widgets = {
            'boatOrBank': RadioSelect(),
        }


class TheContactForm(ModelForm):
    class Meta:
        model = TheContact
        fields = '__all__'


class TheCatchForm(ModelForm):
    class Meta:
        model = TheBigOne
        fields = '__all__'
