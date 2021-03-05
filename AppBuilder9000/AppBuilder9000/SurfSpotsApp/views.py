from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SurfSpotForm
from .models import SurfSpot


# Home page ------------
def surfApp_home(request):
# get the list of spotNames to show your list of favorite spots on the home page
    spots = SurfSpot.objects.all()
    context = {'spots': spots}
# link to home page and display requested content
    return render(request, 'surfApp/surfApp_home.html', context)


# Add Spot page-----use model to create a form and post to database
def surfApp_addSpot(request):
# gets requested form if exists
    form = SurfSpotForm(request.POST or None)
    if form.is_valid():
#  checks that form has the required entries filled in and if
#  valid with no errors, saves to the database
        form.save()
# when done with saving form, this redirects to the index (list of spots) page
        return redirect('SpotIndex')

    else:
# if not saved, print errors to the terminal
        print(form.errors)
        form = SurfSpotForm()
    context = {'form': form, }
    return render(request, 'surfApp/surfApp_addSpot.html',  context)


# Index page---- use index function to get database objects and render them on the index page.
def surfApp_index(request):
# gets all posts from database
    spots = SurfSpot.objects.all()
# print to terminal to make sure data is populating
    print(spots)
# creates dictionary for items in the database and passes the args to the page
    context = {'spots': spots, }
    return render(request, 'surfApp/surfApp_index.html', context)


#  Details page---- use primary key to get details from that item
def surfApp_details(request, pk):
# gets a single instance of the SurfSpot model object from the database
    spot = get_object_or_404(SurfSpot, pk=pk)
    context = {'spot': spot, }
    return render(request, 'surfApp/surfApp_details.html', context)


# Update page (edit)----
def surfApp_update(request, pk):
# means Django expects an integer value and will transfer it to a view as a variable called pk
    pk = int(pk)
    spot = get_object_or_404(SurfSpot, pk=pk)
# HTTP method POST-- finds the form that was submitted by a user
    if request.method == 'POST':
# and we can find that forms filled out answers with the request.POST
        form = SurfSpotForm(request.POST, instance=spot)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('SpotIndex')
        else:
            print(form.errors)
    else:
        form = SurfSpotForm(instance=spot)
        context = {'form': form, }
    return render(request, 'surfApp/surfApp_update.html', context)


# Delete -- from details page, get instance of spot
def surfApp_delete(request, pk):
    pk = int(pk)
    spot = get_object_or_404(SurfSpot, pk=pk)
    if request.method == 'POST':
        return redirect('SpotIndex')
    context = {'spot': spot, }
    return render(request, 'surfApp/surfApp_delete.html', context)


# Confirm delete-- renders delete page for confirmation of action
def confirm_delete(request, pk):
    pk = int(pk)
    spot = get_object_or_404(SurfSpot, pk=pk)
    if request.method == 'POST':
        spot.delete()
        return redirect('SurfSpotsHome')
    else:
        return redirect('SurfSpotsHome')

