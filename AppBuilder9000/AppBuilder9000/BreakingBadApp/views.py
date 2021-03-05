from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Episode
from .forms import EpisodeForm


def breakingbad_home(request):
    return render(request, "BreakingBadApp/BreakingBadApp_home.html", )


def breakingbad_addepisode(request):
    form = EpisodeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BreakingBadHome')
    context = {'form': form}
    return render(request, "BreakingBadApp/BreakingBadApp_addepisode.html", context)


def breakingbad_savedepisodes(request):
    episodes = Episode.Episodes.all()
    paginator = Paginator(episodes, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "BreakingBadApp/BreakingBadApp_index.html", {'page_obj': page_obj})
