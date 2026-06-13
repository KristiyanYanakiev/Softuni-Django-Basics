from django.shortcuts import get_object_or_404

from travelers.models import Traveler


class TravelerActivityMixin:
    def get_travelers_reviews(self, traveler):
        reviews = traveler.reviews.all()

        return reviews


