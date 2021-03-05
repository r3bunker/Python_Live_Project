from django.forms import ModelForm
from .models import FestivalReview

class ReviewForm(ModelForm):
    class Meta:
        model = FestivalReview
        fields = '__all__'