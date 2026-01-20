from django.shortcuts import render, get_object_or_404

from books.models import Book


# Create your views here.
def book_list(request):

    books = Book.objects.all()


    context = {
        'books': books,

    }

    return render(request, 'books/list.html', context)

def book_details(request, pk):

    book = get_object_or_404(Book, pk=pk)

    context = {
        'book': book
    }

    return render(request, 'books/details.html', context)