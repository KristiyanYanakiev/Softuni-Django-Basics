from django.urls import path

from reviews.views import book_reviews, recent_views

urlpatterns = [
    path('', recent_views, name='recent_views'),
    path('<slug:slug>', book_reviews, name='review')
]

