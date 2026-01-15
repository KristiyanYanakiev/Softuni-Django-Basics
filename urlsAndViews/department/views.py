from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'home.html', {'pk': pk})

def view_types_home_view(request):
    return HttpResponse('Home page')

def show_department_by_name(request, department_name: str):
    context = {
        'department_name': department_name
    }
    return render(request, 'department_by_name.html', context)

def index(request, id: int):
    return HttpResponse(f"The id is {id}")

def slug_view(request, slug: str):
    return HttpResponse(f"This is a slug view and the slug is: {slug}")

def path_view(request, path: str):
    return HttpResponse(f"This is a path review with the path: {path}")

def uuid_view(request, uuid: str):
    return HttpResponse(f"{uuid} is a {type(uuid)}", content_type='text/plain')

def redirect_view(request, pk):
    return redirect('home', pk=pk)