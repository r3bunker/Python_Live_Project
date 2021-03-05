from django.shortcuts import render
from .forms import Createsighting
from .models import sighting


def home(request):
    return render(request, 'PokeDex/PokeDex_home.html')


def Sighting(request):
    # create object of form
    form = Createsighting(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    context = {
        'form': form
    }
    return render(request, "PokeDex/PokeDex_sighting.html", context)


def report(request):
    reports = sighting.Sightings.all()
    return render(request, 'PokeDex/PokeDex_index.html', {'reports': reports})


def details(request, pk):
    poke_details = sighting.Sightings.get(pk=pk)
    entry = sighting.Sightings.values_list('Pokemon_notes', flat=True)
    totalList = list(entry)
    content = totalList[pk - 1]

    entry1 = sighting.Sightings.values_list('Pokemon_Name', flat=True)
    print(entry1)
    totalnamel = list(entry1)
    pname = totalnamel[pk - 1]







    context = {
        'poke_details': poke_details,
        'content' : content,
        'pname': pname
    }
    #print(pk)
    return render(request, 'PokeDex/PokeDex_details.html', context)
