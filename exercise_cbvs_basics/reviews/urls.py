from django.urls import path

from reviews.views import AddReview

urlpatterns = [
    path('<int:destination_pk>/add-review/', AddReview.as_view(), name='add-review'),
]