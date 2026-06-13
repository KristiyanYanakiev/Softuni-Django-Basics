from django.shortcuts import get_object_or_404

from travelers.models import Traveler


class TravelerActivityMixin:
    def get_travelers_reviews(self, traveler):

        return traveler.reviews.all()

    def get_travelers_destinations(self, traveler):

        return traveler.destinations.all()


