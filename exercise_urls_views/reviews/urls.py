from django.urls import path

import reviews.views
from reviews.views import recent_reviews

urlpatterns = [
    path('', recent_reviews, name='list' )
]