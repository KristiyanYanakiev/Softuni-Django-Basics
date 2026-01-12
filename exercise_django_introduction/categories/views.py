from django.shortcuts import render

from categories.models import Category


# Create your views here.
def index(request):

    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'list_categories.html', context)
