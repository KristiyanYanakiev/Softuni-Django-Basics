

from django.urls import path, include

from books.views import book_list, book_details, create_book, edit_book, delete_book

app_name = 'books'

urlpatterns = [
    path('', book_list, name='list'),
    path('create_book', create_book, name='create'),
    path('<int:pk>', include([
        path('', book_details, name='book_details'),
        path('edit_book/', edit_book, name='edit'),
        path('delete_book/', delete_book, name='delete')
    ]))
]