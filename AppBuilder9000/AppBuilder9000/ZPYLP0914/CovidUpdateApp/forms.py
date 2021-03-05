from django.forms import ModelForm, RadioSelect
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'covid_Question': RadioSelect
        }
