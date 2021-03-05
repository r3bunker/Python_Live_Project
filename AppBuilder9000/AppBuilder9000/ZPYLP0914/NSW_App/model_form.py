from django.forms import ModelForm, SelectDateWidget, Select
from .models import *

search = 'search'


class AddGameForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddGameForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Game
        fields = ['title', 'publisher', 'user_rating', 'release_date', 'genre', 'ESRB_rating']
        widgets = {
            'user_rating': Select(attrs={'choices': USER_RATINGS}),
            'genre': Select(attrs={'choices': GENRES}),
            'ESRB_rating': Select(attrs={'choices': ESRB_RATINGS}),
            'release_date': SelectDateWidget,
        }
        help_texts = {
            'user_rating': 'Key: 0 - Dumpster Fire | 5 - GOAT'
        }