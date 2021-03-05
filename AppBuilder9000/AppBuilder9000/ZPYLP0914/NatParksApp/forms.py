# from django.forms import ModelForm, DateInput
# from .models import natParksReview
# from .models import NewsletterUser
# from django import forms
#
#
# # form for parks review page
# class DateInput(forms.DateInput):
#     input_type = 'date'
#     input_type = 'date'
#
#
# class NatParksForm(ModelForm):
#     class Meta:
#         model = natParksReview
#         fields = '__all__'
#         widgets = {
#             'date_arrived': DateInput(),
#             'date_departed': DateInput()
#         }
#
#
# class NewsletterUserSignUpForm(forms.ModelForm):
#     class Meta:
#         model = NewsletterUser
#         fields = ['email']
#
#         def clean_email(self):
#             email = self.cleaned_data.get('email')
#
#             return email
