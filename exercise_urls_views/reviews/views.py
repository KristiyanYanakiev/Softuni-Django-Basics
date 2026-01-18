from django.shortcuts import render

from reviews.models import Review


# Create your views here.
def recent_reviews(request):
    reviews = Review.objects.order_by('-created_at')[:5]


    context = {
        'reviews': reviews,
        'page_name': 'Recent reviews'
    }

    return render(request, 'reviews/list.html', context)