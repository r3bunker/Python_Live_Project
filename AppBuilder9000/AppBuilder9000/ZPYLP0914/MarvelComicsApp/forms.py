from django.forms import ModelForm, DateInput
from .models import Subscriber


class CreateSubscriber(ModelForm):
    class Meta:
        #grabbing the model 'Subscriber' and putting it in the variable 'model'
        model = Subscriber
        #display all fields from the 'Subscriber' model
        fields = '__all__'
        #use the default django widget 'DateInput' for the 'sub-dob' field in the 'Subscriber' model
        widgets = {
            'sub_dob': DateInput(attrs={'type': 'date'})
        }

