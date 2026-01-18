from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from destinations.models import Destination


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Welcome to our travel application!')

def destination_list(request):
    destinations = Destination.objects.all()

    context = {
        'destinations': destinations,
        'page_name': 'All Destination'
    }

    return render(request, 'destinations/list.html', context)