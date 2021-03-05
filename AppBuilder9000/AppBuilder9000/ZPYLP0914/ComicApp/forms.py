from django.forms import ModelForm, RadioSelect, PasswordInput, DateInput
from .models import ComicUser, ComicReview


class DateInput(DateInput):
    input_type = 'date'


class SignUpForm(ModelForm):
    class Meta:
        model = ComicUser
        fields = ['username', 'email', 'birth_date', 'password']
        widgets = {'password': PasswordInput(),
                   'birth_date': DateInput()
                   }


class ReviewForm(ModelForm):
    class Meta:
        model = ComicReview
        fields = ['series', 'issue', 'rating', 'review', 'user']
        widgets = {'rating': RadioSelect()}
