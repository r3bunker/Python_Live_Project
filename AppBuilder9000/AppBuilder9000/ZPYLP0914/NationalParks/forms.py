from django.forms import ModelForm , Textarea , DateInput
from .models import ParksInformation


class InfoForm(ModelForm):
    class Meta:
        model = ParksInformation
        fields = '__all__'
        widgets = {
            'Comments': Textarea(),
            'TodaysDate': DateInput(attrs={'type': 'date'})
        }




