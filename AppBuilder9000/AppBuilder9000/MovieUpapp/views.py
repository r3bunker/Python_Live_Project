from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm

def Movie_home(request):
    return render(request, 'MovieUpapp/MovieUpHome.html')

def createItem(request):
    form = MovieForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MovieUpHome')
    else:
        print(form.errors)
        form = MovieForm()
    context = {'form': form}
    return render(request, 'MovieUpapp/createItem.html', context)
