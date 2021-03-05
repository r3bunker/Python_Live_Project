from django.shortcuts import render, redirect, get_object_or_404
from .models import Climb, Attempt
from .forms import ClimbForm, AttemptForm
from django.contrib import messages

#-- GLOBAL VARIABLES --
global climb_form
global attempt_form


def sendit_home(request):
    return render(request, 'SendItApp/SendItApp_home.html')


def my_sends(request):
    climbs = Climb.objects.all()
    attempts = Attempt.objects.all()
    return render(request, 'SendItApp/SendItApp_my_sends.html', {'climbs': climbs, 'attempts': attempts})


# -- BLANK CLIMB/ATTEMPT FORMS --
def create(request):
    global climb_form
    global attempt_form
    climb_form = ClimbForm()
    attempt_form = AttemptForm()
    return render(request, 'SendItApp/SendItApp_create.html',
                  {'climb_form': climb_form, 'attempt_form': attempt_form})


#-- CREATE FUNCTIONS --
def climb_create(request):
    global climb_form
    global attempt_form
    if request.method == "POST":
        climb_form = ClimbForm(request.POST)
        if climb_form.is_valid():
            climb_form.save()
            messages.success(request, 'Success: Climb was added')
            return redirect('/SendItApp/climb_create/#climb-form')
        else:
            print(climb_form.errors)
            messages.warning(request, 'FAIL: CLIMB NOT ADDED!')
            return redirect('SendItApp/climb_create/#climb-form')
    else:
        climb_form = ClimbForm()
        attempt_form = AttemptForm()
    return render(request, 'SendItApp/SendItApp_create.html',
                  {'climb_form': climb_form, 'attempt_form': attempt_form})


def attempt_create(request):
    global climb_form
    global attempt_form
    if request.method == "POST":
        attempt_form = AttemptForm(request.POST)
        if attempt_form.is_valid():
            attempt_form.save()
            messages.success(request, 'Success: Attempt was added')
            return redirect('/SendItApp/attempt_create/#attempt-form')
        else:
            print(attempt_form.errors)
            messages.warning(request, 'FAIL: ATTEMPT NOT ADDED!')
            return redirect('SendItApp/attempt_create/#attempt-form')
    else:
        climb_form = ClimbForm()
        attempt_form = AttemptForm()
    return render(request, 'SendItApp/SendItApp_create.html',
                  {'climb_form': climb_form, 'attempt_form': attempt_form})


#-- DETAIL FUNCTIONS --
def climb_detail(request, pk):
    global climb_form
    global attempt_form
    pk = int(pk)
    # -- GET THE ITEM FROM CLIMB MODEL
    climbs = Climb.objects.get(id=pk)
    climb = get_object_or_404(Climb, pk=pk)
    # -- RECORD ALL ATTEMPTS TO REQUESTED CLIMB ITEM
    attempt = climb.attempt_set.all()
    attempt_count = attempt.count()
    # -- CREATE FORM TO BE SHOWN WITH REQUESTED ITEM

    climb_form = ClimbForm(data=request.POST or None, instance=climb)
    return render(request, 'SendItApp/SendItApp_climb_details.html',
                  {'climb': climb, 'climbs': climbs, 'attempt': attempt, 'climb_form': climb_form, 'attempt_count': attempt_count})


def attempt_detail(request, pk):
    global climb_form
    global attempt_form
    pk = int(pk)
    attempt = Attempt.objects.get(id=pk)
    climb = attempt.climb
    # -- CREATE FORM TO BE POPULATED WITH REQUEST
    attempt_instance = get_object_or_404(Attempt, pk=pk)
    attempt_form = AttemptForm(data=request.POST or None, instance=attempt_instance)
    return render(request, 'SendItApp/SendItApp_attempt_details.html',
                  {'attempt': attempt, 'climb': climb, 'attempt_form': attempt_form})


#-- EDIT FUNCTIONS
def climb_edit(request, pk):
    global climb_form
    pk = int(pk)
    # CREATE A FORM THAT SHOWS REQUESTED CLIMB ITEM
    climb = get_object_or_404(Climb, pk=pk)
    climb_form = ClimbForm(data=request.POST or None, instance=climb)
    # FORM VALIDATION WITH DISPLAY OF 'CLIMB UPDATED'
    if climb_form.is_valid():
        climb_form.save()
        messages.success(request, 'Climb Updated', extra_tags='climb')
    else:
        print(climb_form.errors)
        messages.warning(request, 'Update Failure', extra_tags='climb')
    return render(request, 'SendItApp/SendItApp_climb_edit.html',
                  {'climb': climb, 'climb_form': climb_form})



def attempt_edit(request, pk):
    global attempt_form
    pk = int(pk)
    # CREATE A FORM THAT SHOWS REQUESTED CLIMB ITEM
    attempt = get_object_or_404(Attempt, pk=pk)
    attempt_form = AttemptForm(data=request.POST or None, instance=attempt)
    # FORM VALIDATION WITH DISPLAY OF 'CLIMB UPDATED'
    if attempt_form.is_valid():
        attempt_form.save()
        messages.success(request, 'Attempt Updated', extra_tags='attempt')
    else:
        print(attempt_form.errors)
        messages.warning(request, 'Update Failure', extra_tags='attempt')
    return render(request, 'SendItApp/SendItApp_attempt_edit.html',
                  {'attempt': attempt, 'attempt_form': attempt_form})
#-- TODO def attempt_edit(request, pk) goes here


# -- DELETE FUNCTIONS
def climb_delete(request, pk):
    pk = int(pk)
    climb = get_object_or_404(Climb, pk=pk)
    climb.delete()
    return redirect('MySends')


def attempt_delete(request, pk):
    pk = int(pk)
    attempt = get_object_or_404(Attempt, pk=pk)
    attempt.delete()
    return redirect('MySends')
