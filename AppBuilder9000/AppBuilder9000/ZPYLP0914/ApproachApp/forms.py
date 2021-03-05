from django.forms import ModelForm
from .models import ApproachUser, Climb, TripManager, Guidebook
from django import forms


class CreateNewUser(ModelForm):
    class Meta:
        model = ApproachUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = '__all__'


class AddClimb(ModelForm):
    class Meta:
        model = Climb
        fields = '__all__'


class AddNewTrip(ModelForm):
    class Meta:
        model = TripManager
        fields = '__all__'


class AddGuideBook(ModelForm):
    class Meta:
        model = Guidebook
        fields = '__all__'
