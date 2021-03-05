from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import TheBigOneForm
from .forms import TheContactForm
from .models import TheBigOne


def home(request):
    return render(request, 'CatchIdentificationApp/CatchIdentification_Home.html')


#def catchindex(request):
#    return render(request, 'CatchIdentificationApp/CatchIdentification_CatchIndex.html')


def contact(request):
    form = TheContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CatchIdentificationAppHome')
    context = {'form': form, }
    return render(request, 'CatchIdentificationApp/CatchIdentification_Contact.html', context)


def catchLog(request):
    form = TheBigOneForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('CatchIdentificationAppHome')
    context = {'form': form, }
    return render(request, 'CatchIdentificationApp/CatchIdentification_BigOne.html', context)


def searchlog(request):
    indexes = TheBigOne.objects.all()
    if request.method == 'GET':
        query = request.GET.get('q')

        if query is not None:
            results = TheBigOne.objects.filter(
                Q(fish_Type__icontains=query) |
                Q(fish_Length__icontains=query) | Q(fish_Weight__icontains=query) |
                Q(tackle_Used__icontains=query) | Q(boatOrBank__icontains=query) |
                Q(body_of_Water__icontains=query)
            )
            context = {'results': results, 'indexes': indexes}

            return render(request, 'CatchIdentificationApp/CatchIdentification_CatchIndex.html', context)

    return render(request, 'CatchIdentificationApp/CatchIdentification_CatchIndex.html', {'indexes': indexes})
