from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import PlayTimeForm
from .models import PlayTime
from .forms import OwnerForm
from .models import Owner



def home(request):
    return render(request, 'PupApp/PupApp_home.html') #links to homepage

def add_pup(request):
    form = PlayTimeForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form to the database

        return redirect('PupHome')
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = PlayTimeForm()                   #Creates a new blank form
    return render(request, 'PupApp/PupApp_create.html', {'form': form})

def add_owner(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PupHome')
    else:
        print(form.errors)
        form = OwnerForm()
    return render(request, 'PupApp/PupApp_createOwner.html', {'ownerform': form})


def index(request):
    get_posts = PlayTime.PlayTime.all() #gets all posts from db
    context = {'PlayTime': get_posts}  #creates dictionary for items in db
    return render(request, 'PupApp/PupApp_index.html', context)

def pupapp_details(request, pk):
    get_posts = get_object_or_404(PlayTime, pk=pk) #single instance of pup entry in db
    context = {'PlayTime': get_posts}   #dictionary object to pass through the page
    return render(request, 'PupApp/PupApp_details.html', context) #open page

#Edits an entry of a pup in DB
def pupapp_edit(request, pk):
    pk = int(pk)
    post = get_object_or_404(PlayTime, pk=pk)
    if request.method == 'POST':
        form = PlayTimeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('pupDetails', pk=pk)
        else:
            print(form.errors)
    else:
        form = PlayTimeForm(instance=post)
        context = {'form': form}
        return render(request, 'PupApp/PupApp_edit.html', context)

#Deletes entry of pup in DB
def pupapp_delete(request, pk):
    pk = int(pk)
    post = get_object_or_404(PlayTime, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('indexPup')
    context = {'post': post}
    return render(request, 'PupApp/PupApp_delete.html',context)

#Confirm deletion of pup in DB
def confirmed(request):
    if request.method =="POST":
        form =PlayTimeForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('index')
    else:
        return redirect('index')
