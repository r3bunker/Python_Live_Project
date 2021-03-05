from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CreateNewUser, AddClimb, AddNewTrip, AddGuideBook
from .models import ApproachUser, TripManager, Guidebook, Climb


def approach_home(request):
    return render(request, 'ApproachApp/PokeDex_home.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user_check = get_object_or_404(ApproachUser, username=username)
        if password == user_check.password:
            return render(request, 'ApproachApp/PokeDex_home.html', {'User': user_check})
        else:
            messages.info(request, 'Invalid Username or Password')
            return render(request, 'ApproachApp/SignIn.html')
    else:
        return render(request, 'ApproachApp/SignIn.html')


def create_user(request):
    form = CreateNewUser(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SignIn')
    else:
        content = {'form': form}
        return render(request, 'ApproachApp/CreateUser.html', content)


def tick_list(request):
    climbs = Climb.view.get_items('pk', 'climb_name', 'climb_grade', 'sent')
    return render(request, 'ApproachApp/TickList.html', {'Climbs': climbs})


def add_climb(request):
    form = AddClimb(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('TickList')
    else:
        content = {'form': form}
        return render(request, 'ApproachApp/AddClimb.html', content)


def view_climb(request, pk):
    climb = Climb.info.filter(pk=pk)
    pk = int(pk)
    climb_info = get_object_or_404(climb, pk=pk,)
    form = AddClimb(instance=climb_info)
    for field in form.fields:
        form.fields[field].disabled = True

    return render(request, 'ApproachApp/ClimbViewer.html', {'form': form, 'Climb': climb})


def trip_manager(request):
    trips = TripManager.view.get_items('pk', 'trip_name', 'start_date', 'end_date')

    return render(request, 'ApproachApp/TripManager.html', {'trips': trips})


def new_trip(request):
    form = AddNewTrip(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('TripManager')
    else:
        content = {'form': form}
        return render(request, 'ApproachApp/CreateNewTrip.html', content)


def view_trip(request, pk):
    trips = TripManager.info.filter(pk=pk)
    pk = int(pk)
    trip_info = get_object_or_404(TripManager, pk=pk,)
    form = AddNewTrip(instance=trip_info)
    for field in form.fields:
        form.fields[field].disabled = True

    return render(request, 'ApproachApp/TripViewer.html', {'form': form, 'trip': trips})


def guidebooks(request):
    guide = Guidebook.view.get_items('pk', 'name', 'price', 'climb_area')
    return render(request, 'ApproachApp/Guidebooks.html', {'guides': guide})


def addguidebook(request):
    form = AddGuideBook(data=request.POST or None)
    if request.method == 'POST':
        form = AddGuideBook(request.POST, request.FILES)  # FOR PILLOW LIBRARY
        if form.is_valid():
            form.save()
            return redirect('GuideBooks')
    else:
        content = {'form': form}
        return render(request, 'ApproachApp/AddGuidebook.html', content)


def view_guidebook(request, pk):
    guide = Guidebook.info.filter(pk=pk)
    pk = int(pk)
    guidebook_info = get_object_or_404(Guidebook, pk=pk,)
    form = AddGuideBook(instance=guidebook_info)
    for field in form.fields:
        form.fields[field].disabled = True

    return render(request, 'ApproachApp/GuidebookViewer.html', {'form': form, 'Guide': guide})


def training(request):
    return render(request, 'ApproachApp/Training.html')
