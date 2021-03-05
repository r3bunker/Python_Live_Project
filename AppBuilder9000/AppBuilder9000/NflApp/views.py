from django.shortcuts import render, redirect, get_object_or_404
from .models import PlayerProfile
from .forms import PlayerForm

def Nfl_home(request):
    return render(request, 'NflApp/NflApp_home.html')

def createPlayer(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('NflHome')
    context = {'form': form}
    return render(request, 'NflApp/createPlayer.html', context)

def NflApp_index(request):
    form = PlayerForm()
    players = PlayerProfile.objects.all()
    print(players)
    context = {'form': form, 'players': players}
    return render(request, 'NflApp/NflApp_index.html', context)

def NflApp_details(request, pk):
    player = get_object_or_404(PlayerProfile, pk=pk)
    context = {'player': player}
    return render(request, 'NflApp/NflApp_details.html', context)

def NflApp_edit(request, pk):
    player = get_object_or_404(PlayerProfile, pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player.save()
            return redirect('NflApp_details', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    context = {'form': form}
    return render(request, 'NflApp/NflApp_edit.html', context)

def NflApp_delete(request, pk):
    player = get_object_or_404(PlayerProfile, pk=pk)
    player.delete()
    return redirect('NflApp_index')



