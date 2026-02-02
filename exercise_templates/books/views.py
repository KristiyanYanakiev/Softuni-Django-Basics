from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from books.forms import BookCreateForm, BookSearchForm
from books.models import Book


# Create your views here.
def book_list(request):
    books = Book.objects.all()

    search_form = BookSearchForm(request.GET or None)
    if 'query' in request.GET: #this 'query" is a key in the Dictionnary request.GET correct?
        if search_form.is_valid():
            books = Book.objects.filter(
                Q(title__icontains=search_form.cleaned_data['query'])
                    |
                Q(description__icontains=search_form.cleaned_data['query'])
            )





    context = {
        'books': books,
        'search_form': search_form

    }

    return render(request, 'books/list.html', context)

def book_details(request, pk):

    book = get_object_or_404(Book, pk=pk)

    context = {
        'book': book
    }

    return render(request, 'books/details.html', context)

def create_book(request: HttpRequest):
    form = BookCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'books/create.html', context)

def edit_book(request: HttpRequest, pk: int ) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = BookCreateForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'books/edit.html', context)


def delete_book(request: HttpRequest, pk: int ) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    form = BookCreateForm(request.POST or None, instance=book)
    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'books/delete.html', context)