from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import User, Game
from .forms import NewUserForm, AddGameForm


def home(request):
    return render(request, 'GamesApp/GamesApp_Home.html')


def create_profile(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GamesAppHome')
    else:
        form = NewUserForm()
    return render(request, 'GamesApp/GamesApp_NewProfile.html', {'form': form})


def add_game(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("GameLibrary")
    else:
        form = AddGameForm()
    return render(request, 'GamesApp/GamesApp_AddGame.html', {'form': form})


def user_index(request):
    users = User.Profiles.all()
    return render(request, 'GamesApp/GamesApp_Index.html', {'users': users})


def details(request, pk):
    game_details = Game.Games.filter(pk=pk)
    return render(request, 'GamesApp/GamesApp_GameInfo.html', {'game_details': game_details})


def game_library(request):
    users_games = Game.Games.all()
    return render(request, 'GamesApp/GamesApp_GameLibrary.html', {'users_games': users_games})


def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = AddGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('GameDetails', pk=game.pk)

    else:
        form = AddGameForm(instance=game)
    return render(request, "GamesApp/GamesApp_EditGame.html", {'form': form})


def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        game.delete()
        return redirect("GameLibrary")
    return render(request, 'GamesApp/GamesApp_DeleteGame.html', {'game': game})

"""
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = NewUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('GamesAppHome', pk=user.pk)

    else:
        form = NewUserForm(instance=user)
    return render(request, "GamesApp/GamesApp_EditUser.html", {'form': form})
"""