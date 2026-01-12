from django.urls import path

from notes.views import first_view

urlpatterns = [
    path('', first_view, name='index')
]