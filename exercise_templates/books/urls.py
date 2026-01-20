from django.urls import path

from books.views import book_list, book_details

app_name = 'books'

urlpatterns = [
    path('', book_list, name='list'),
    path('<int:pk>', book_details, name='book_details')
]