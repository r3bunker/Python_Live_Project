from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'Home/index.html')

def index(request):
    return render(request, 'Acu_Insurance/Acu_Insurance_base.html')



