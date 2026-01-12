from django.urls import path

from categories.views import index
from notes.views import first_view

urlpatterns = [
    path('', index, name='list_categories')
]