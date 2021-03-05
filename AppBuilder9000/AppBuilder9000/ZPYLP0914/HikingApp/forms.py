from django.forms import ModelForm
from .models import create_happ_user, hike_preferences


class create_new_happ_user(ModelForm):
    class Meta:
        # selected model is create_happ_user
        model = create_happ_user
        # model fields to be include in form is all
        fields = '__all__'


class survey(ModelForm):
    class Meta:
        # selected model is hike_preferences
        model = hike_preferences
        # model fields to be include in form is all
        fields = '__all__'
