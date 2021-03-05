from django.shortcuts import render, redirect, get_object_or_404
from .forms import EncounterForm
from .models import Encounter


def Bigfoot_home(request):
    return render(request, 'BigfootApp/Bigfoot_Home.html')


def submission(request):
    return render(request, 'BigfootApp/Bigfoot_Submit.html')


def report_deleted(request):
    return render(request, 'BigfootApp/Bigfoot_Submit_Delete.html')


def report_edited(request):
    return render(request, 'BigfootApp/Bigfoot_Submit_Edit.html')


def new_encounter(request):
    form = EncounterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('submission')
    else:
        print(form.errors)
        form = EncounterForm()
    context = {'form': form}
    return render(request, 'BigfootApp/Bigfoot_CreateEncounter.html', context)


def encounter_index(request):
    encounters = Encounter.objects.all()
    context = {'encounters': encounters}
    return render(request, 'BigfootApp/Bigfoot_Index.html', context)


def encounter_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Encounter, pk=pk)
    form = EncounterForm(data=request.POST or None, instance=item)
    return render(request, 'BigfootApp/Bigfoot_Details.html', {'form': form})


def encounter_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Encounter, pk=pk)
    if request.method == 'POST':
        form = EncounterForm(request.POST, instance=item)
        if form.is_valid():
            item.save()
            return redirect('report_edited')
    else:
        form = EncounterForm(instance=item)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'BigfootApp/Bigfoot_Edit.html', context)


def encounter_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Encounter, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('report_deleted')
    context = {'item': item}
    return render(request, "BigfootApp/Bigfoot_Delete.html", context)







