from django.urls import path

from reviews.views import AddReview, ReviewListView

app_name = 'reviews'

urlpatterns = [
    path('<int:destination_pk>/add-review/', AddReview.as_view(), name='add-review'),
    path('list/', ReviewListView.as_view(), name='list')
]