from django.shortcuts import render

import homepage


# Create your views here.
def index(request):
    return render(request, 'base.html')