from django.shortcuts import render, get_object_or_404

from books.models import Book
from reviews.models import Review


# Create your views here.
def book_reviews(request, slug):
    book = get_object_or_404(Book, slug=slug)
    reviews = book.reviews.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/review_details.html', context)

def recent_views(request):
    reviews = Review.objects.order_by('-created_at')[:1]

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/list.html', context)