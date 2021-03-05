import requests
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from .models import BookReview
from .forms import ReviewForm
from django.contrib import messages
from bs4 import BeautifulSoup

# Create your views here.


# Display Home page

def home(request):
    return render(request, 'SFReview/SFR_home.html') #Link to the home page of the project.

#Display creation confirmation page

def sfr_createconf(request):
    return render(request, 'SFReview/SFR_createconf.html') #Link to the home page of the project.

# Add details int URL for form creation

def sfr_previousreview(request):
    get_review = BookReview.reviews.all() #Get current reviews from database
    context = {'BookReview': get_review} #Creates dictionary object for reviews
    return render(request, 'SFReview/SFR_previous.html', context)

# Add a review to the DB


def sfr_createreview(request):
    if request.method == "POST" or None:
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            print(form)
            print("Valid Form")
            form.save()
            return render(request, 'SFReview/SFR_createconf.html', {'form': form})
        else:
            print(form)
            print("Invalid Form")
            print(form.errors)
            return render(request, 'SFReview/SFR_create.html', {'form': form})
    else:
        return render(request, 'SFReview/SFR_create.html')

#Detail page

def sfr_details(request, pk):
    pk = int(pk)                                   #Value of Pk to int(primary key) making sure proper data type.
    review = get_object_or_404(BookReview, pk=pk)  #Single instance of a review from the db.
    context={'review': review}                     #Dictionary object to pass through to the page
    return render(request, 'SFReview/SFR_details.html', context) #Open the page.

#Edit Details page

def sfr_edit(request, pk):
    pk = int(pk)
    review = get_object_or_404(BookReview, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid(): #form validation
            review = form.save()
            review.save()
            return redirect('details', pk=review.pk) #back to the detail page
    else:
        form = ReviewForm(instance=review)
    context={'form': form, 'pk': pk, 'review': review.Title}
    return render(request, 'SFReview/SFR_edit.html', context)

def sfr_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(BookReview, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('PreviousReview')
    context = {'item': item,}
    return render(request, 'SFReview/SFR_deleteconf.html', context)

def sfr_delconf(request):
    if request.method == 'POST':
        #Creates the form instance, binds the data to it.
        form = BookReview(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('SFReview/Previous')
        else:
            return redirect('SFReview/Previous')

# Beautiful Soup Scraper:

def sfr_goodreads(request):
    # Website to scrap:
    source = requests.get('https://www.goodreads.com/book/popular_by_date/2020/10?ref=nav_brws_newrels').text
    # Soup
    soup = BeautifulSoup(source, 'html.parser')
    # Return each book cell and all data in it.
    resultTR = soup.find_all('tr')

    bookList = []
    # Filter down for specific booktitle, author, and img src.
    for item in resultTR:
        Author = item.find(class_='authorName')
        narrowAuthor = Author.find(itemprop='name')
        resultAuthor = narrowAuthor.get_text()

        BookTitle = item.find(class_='bookTitle')
        narrowBookTitle = BookTitle.find(itemprop='name')
        resultBookTitle = narrowBookTitle.get_text()
            # Pull img src without extra code.
        if item.img:
            resultImg = item.img['src']
        else:
            resultImg = 'No image found'
        # Dictionary to track and relate the title, author and image.
        bookCombo = {"Title": resultBookTitle, "Author": resultAuthor, "CoverImg": resultImg}

        # List to keep each book object in.
        bookList.append(bookCombo)


    print(bookList)

    return render(request, 'SFReview/SFR_goodreads.html', {'books':bookList}) # Link to reveiws scrapped with beautiful soup.