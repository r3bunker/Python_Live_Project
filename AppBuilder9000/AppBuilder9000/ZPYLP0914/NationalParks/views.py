from django.shortcuts import render, redirect , get_object_or_404
from django.http import Http404
from .forms import InfoForm
from .models import ParksInformation


def index(request):
    return render(request, 'NationalParks/home.html')

def Reviews(request):
    # if this is a POST request we need to process the form data
    # create a form instance and populate it with data from the request:
    form = InfoForm(request.POST or None)
    # check whether it's valid
    if request.method == 'POST':
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return redirect('Submitted')

    else:

        context = {
            'form': form
        }
        # redirect to a new url:
        return render(request, 'NationalParks/reviews.html', context)

#this function sends the All of the data to the desired template as a dictionary form
def Submitted(request):
    parks = ParksInformation.objects.all()
    return render(request, 'NationalParks/Feedback.html', {'parks': parks})


def details(request, pk):
    try:
        Parks = ParksInformation.objects.get(pk=pk)
    except ParksInformation.DoesNotExist:
        raise Http404('This park does not exist')
    return render(request, 'NationalParks/details.html', {'Parks': Parks})

def delete(request, pk):
    pk = int(pk)
    park = get_object_or_404(ParksInformation, pk=pk)
    if request.method == 'POST':
        park.delete()
        return redirect('Submitted')
    context = {'park': park}
    return render(request,'NationalParks/confirmdelete.html', context )

def edit(request,pk):
    pk = int(pk)
    park = get_object_or_404(ParksInformation, pk=pk)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=park)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            park = form.save()
            park.save()
            return redirect('details', pk=park.pk)
    else:
        form = InfoForm(instance=park)
    context = {
        'form': form , 'pk': pk
     }
     # redirect to a new url:
    return render(request, 'NationalParks/edit.html', context)

