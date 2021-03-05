from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import player
from django.http import Http404


def soccer_home(request):
    return render(request, 'SoccerApp/SoccerApp_home.html')

def Addplayer(request):
    #create form
    form = PlayerForm(request.POST or None)

    #check if form is valid
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Submit')

    else:

        context = {
            'form': form
        }
        # redirect to a new url:
        return render(request, 'SoccerApp/SoccerApp_addplayer.html', context)


def Submit(request):
    adds = player.objects.all()
    context = {'adds': adds}
    return render(request, 'SoccerApp/SoccerApp_index.html', context)


def details(request, pk):
    try:
        Adds = player.objects.get(pk=pk)
    except player.DoesNotExist:
        raise Http404('Player not available')
    return render(request, 'SoccerApp/SoccerApp_details.html', {'Adds': Adds})


def delete(request, pk):
    pk = int(pk)
    add = get_object_or_404(player, pk=pk)
    if request.method == 'POST':
        add.delete()
        return redirect('Submit')
    context = {'add': add}
    return render(request, 'SoccerApp/SoccerApp_delete.html', context)


def edit(request, pk):
    pk = int(pk)
    add = get_object_or_404(player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=add)
        if form.is_valid():
            add = form.save()
            add.save()
            return redirect('Details', pk=add.pk)
    else:
        form = PlayerForm(instance=add)
    context = {
        'form': form, 'pk': pk
     }
    return render(request, 'SoccerApp/SoccerApp_edit.html', context)
