from django.shortcuts import render, redirect
from django.contrib import messages
from .model_form import AddGameForm
from .models import Game

def NSW_APP_Homepage(request):
    return render(request, 'NSW_App/NSW_App_home.html')

def NSW_APP_About(request):
    return render(request, 'NSW_App/NSW_App_about.html')

def NSW_News_API(request):
    return render(request, 'NSW_App/NSW_App_API.html')

def Current_Games_Index(request):
    return render(request, 'NSW_App/NSW_App_Current_Games.html')

def Future_Games_Index(request):
    return render(request, 'NSW_App/NSW_App_Future_Games.html')

def Add_Game(request):
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Game Added to Library!')
            return redirect("UserLibrary")
    else:
        form = AddGameForm()
    return render(request, 'NSW_App/NSW_App_form.html', {'form': form})

def User_Library(request):
    user_games = Game.objects.all()
    content = {
        'user_games': user_games,
    }
    return render(request, 'NSW_App/NSW_App_Library.html', content)

def Details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game
    }
    return render(request, 'NSW_App/NSW_App_details.html', context)