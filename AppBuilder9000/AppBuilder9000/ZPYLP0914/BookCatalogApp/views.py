from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Book
from .forms import BookForm

#  Link to the home page of the project.
def book_home(request):
    return render(request, 'BookCatalogApp/BCA_home.html')

# need to render all fields from the form.  Able to create the form object and to check the form..
def CreateView(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookCatalogApp:book_home')
    else:
        form = BookForm()
        context = {'form':form}
        return render(request,'BookCatalogApp/BCA_create_record.html',context)

def Retrieve_ListView(request):
    dataset = Book.books.all()
    return render(request, 'BookCatalogApp/BCA_listview.html', {'dataset':dataset})

def Retrieve_DetailView(request, id):
    try:
        data = Book.books.get(id=id)
    except Book.books.DoesNotExist:
        raise Http404('Data does not exist')

    return render(request, 'BookCatalogApp/BCA_detailview.html', {'data':data})

# def UpdateView(request, id):
#     try:
#         old_data = get_object_or_404(Book, id=id)
#     except Exception:
#         raise Http404('Does Not Exist')
#
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=old_data)
#         if form.is_valid():
#             form.save()
#             return redirect('BookCatalogApp:list_index')
#         else:
#             form = BookForm(instance=old_data)
#         context = {'form':form}
#         return render(request, 'BookCatalogApp:BCA_update.html{id}', context)
#
# def DeleteView(request,id):
#     try:
#         data = get_object_or_404(Book,id =id)
#     except Exception:
#         raise Http404('Does Not Exist')
#
#     if request.method == 'POST':
#         data.delete()
#         return redirect('BookCatalogApp:list_index')
#     else:
#         return render(request, 'BookCatalogApp:BCA_delete.html')
