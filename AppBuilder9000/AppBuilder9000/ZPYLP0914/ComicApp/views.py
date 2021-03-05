from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, ReviewForm
from .models import ComicReview
from django.core.paginator import Paginator


def home(request):
    return render(request, 'ComicApp/ComicApp_Home.html')


def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ComicHome')
    return render(request, 'ComicApp/ComicApp_SignUp.html', {'form': form})


def review(request):
    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ComicHome')
    return render(request, 'ComicApp/ComicApp_ReviewCreate.html', {'form': form})


def review_index(request):
    order_by = request.GET.get('order_by')
    direction = request.GET.get('direction')
    if direction == 'desc' and order_by[0] != '-':
        order_by = '-{}'.format(order_by)
        reviews = ComicReview.reviews.all().order_by(order_by)
    elif direction == 'asc' and order_by[0] == '-':
        order_by = order_by[1:]
        reviews = ComicReview.reviews.all().order_by(order_by)
    elif direction == 'asc':
        reviews = ComicReview.reviews.all().order_by(order_by)
    else:
        reviews = ComicReview.reviews.all()

    paginator = Paginator(reviews, 5)  # Show 5 reviews per page.
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'order_by': order_by, 'direction': direction, 'reviews': reviews}
    return render(request, 'ComicApp/ComicApp_ReviewIndex.html', context)


def review_details(request, review_id):
    user_review = get_object_or_404(ComicReview, pk=review_id)
    return render(request, 'ComicApp/ComicApp_ReviewDetails.html', {'user_review': user_review})


def review_edit(request, review_id):
    user_review = get_object_or_404(ComicReview, pk=review_id)
    form = ReviewForm(instance=user_review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=user_review)
        if form.is_valid():
            form.save()
            return redirect('ComicReviewIndex')
    return render(request, 'ComicApp/ComicApp_ReviewEdit.html', {'form': form})


def review_delete(request, review_id):
    user_review = get_object_or_404(ComicReview, pk=review_id)
    if request.method == 'POST':
        user_review.delete()
        return redirect('ComicReviewIndex')
    return render(request, 'ComicApp/ComicApp_ReviewDetails.html', {'user_review': user_review})
