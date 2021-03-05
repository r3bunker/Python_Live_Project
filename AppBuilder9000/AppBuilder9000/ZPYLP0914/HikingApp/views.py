from django.shortcuts import render, redirect, get_object_or_404
from .forms import create_new_happ_user, survey
from .models import hike_preferences


def home(request):
    # returns home page
    return render(request, 'HikingApp/HikingApp_Home.html')


def details(request, pk):
    # detail is = to selected data
    detail = get_object_or_404(hike_preferences, pk=pk)
    # content is = to the dictionary value and object
    content = {'detail': detail}
    # returns detail page and selected db content
    return render(request, 'HikingApp/HikingApp_Details.html', content)


def survey_result(request):
    # survey_results is = to all data in db
    survey_results = hike_preferences.admin.all()
    # content is equal to dictionary value and object
    content = {'survey_results': survey_results, }
    # returns survey results page and all db content
    return render(request, 'HikingApp/HikingApp_SurveyResults.html', content)


def daily_survey(request):
    # form is = to form survey and will post to the db
    form = survey(data=request.POST or None)
    # if the method is post
    if request.method == 'POST':
        # if the form is valid
        if form.is_valid():
            # save form
            form.save()
        # redirect to happ home
        return redirect('happ_home')
    # renders the Survey page and form
    return render(request, 'HikingApp/HikingApp_Survey.html', {'form': form})


def create_the_happ_user(request):
    # form is = to form create new happ user and will post to db
    form = create_new_happ_user(data=request.POST or None)
    # if the method is post
    if request.method == 'POST':
        # if the form is valid
        if form.is_valid():
            # save form
            form.save()
            # redirect to happ_home
            return redirect('happ_home')
    # renders the MyProfile page and form
    return render(request, 'HikingApp/HikingApp_MyProfile.html', {'form': form})
