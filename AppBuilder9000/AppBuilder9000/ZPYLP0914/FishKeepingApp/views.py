from django.shortcuts import render, redirect, get_object_or_404
from .models import FishKeepingUser, FishWishList
from .forms import CreateUserForm, CreateWishListForm


def home(request):
    # The form is the CreateWishListForm
    form = CreateWishListForm(data=request.POST or None)
    # If the request is a POST request
    if request.method == 'POST':
        # Primary key is the account
        pk = request.POST['account']
        # Return parameters for function to show wish list
        return FishKeeping_ShowWishList(request, pk)
    # content is the form dictionary
    content = {'form': form}
    # render form in home template
    return render(request, 'FishKeepingApp/FishKeeping_home.html', content)


def FishKeeping_Details(request, pk):
    fish_details = get_object_or_404(FishWishList, pk=pk)
    # account = get_object_or_404(FishKeepingUser, pk=pk)
    content = {'fish_details': fish_details}  # 'account': account}
    return render(request, 'FishKeepingApp/FishKeeping_Details.html', content)


def FishKeeping_ShowWishList(request, pk):
    # account either gets the user as the primary key or returns a 404
    account = get_object_or_404(FishKeepingUser, pk=pk)
    # Filters all Fish data related to current account's name
    # as the primary key, within the FishWishList
    fish = FishWishList.Fish.filter(account=pk)
    # Test to find out whether fish variable was printing to terminal
    print("These are the fish:")
    print(fish)
    # content is the dictionary containing the account and the fish
    content = {'account': account, 'fish': fish}
    # render content to html template
    return render(request, 'FishKeepingApp/FishKeeping_WishList2.html', content)


def FishKeeping_CreateUser(request):
    form = CreateUserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('FishKeepingHome')
    content = {'form': form}
    return render(request, 'FishKeepingApp/FishKeeping_CreateUser.html', content)


def FishKeeping_WishList(request):
    form = CreateWishListForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('FishKeepingHome')
    content = {'form': form}
    return render(request, 'FishKeepingApp/FishKeeping_WishList.html', content)
