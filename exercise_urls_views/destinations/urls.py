from django.urls import path

from destinations.views import index, destination_list

urlpatterns = [
    path('', index, name='home'),
    path('destinations/', destination_list, name = 'list'),

]