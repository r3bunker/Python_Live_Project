from django.forms import DateField, DateInput, ModelForm
from .models import Episode


class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = '__all__'

    episode_date = DateField(widget=DateInput(attrs={'placeholder': 'mm/dd/yy'}))
