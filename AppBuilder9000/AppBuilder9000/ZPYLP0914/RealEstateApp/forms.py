from django.forms import ModelForm, RadioSelect

from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

                        #options to choose from/or to set later
class PrimaryBankForm(ModelForm):
    class Meta:
        model = PrimaryBank
        fields = '__all__'
        widgets = {
            'Bank of America': RadioSelect(),
            'Fifth Third Bank': RadioSelect(),
            'First Citizens Bank': RadioSelect(),
            'Wells Fargo': RadioSelect(),
            'Capital Bank': RadioSelect(),
            'Other': RadioSelect()
        }
