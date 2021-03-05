from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def Covidhome(request):
    return render(request, 'CovidUpdateApp/Covidhome.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Covidhome')
    context = {'form': form, }
    return render(request, 'CovidUpdateApp/CovidUpdate_covidcontact.html', context)


# This creates the index page where the db info will be displayed
def covidIndex(request):
    covid_view = Contact.objects.all()
    context = {'covid_view': covid_view}
    return render(request, 'CovidUpdateApp/CovidUpdate_index.html', context)


def inputDetails(request, pk):
    covid_view = Contact.objects.get(pk=pk)
    print(covid_view)
    context = {'covid_view': covid_view}
    return render(request, 'CovidUpdateApp/CovidUpdate_details.html', context)
