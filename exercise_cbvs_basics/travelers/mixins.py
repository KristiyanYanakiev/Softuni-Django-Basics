from django.db.models import F
from django.shortcuts import get_object_or_404

from travelers.models import Traveler


class TravelerActivityMixin:
    def get_travelers_reviews(self, traveler):

        return traveler.reviews.all()

    def get_travelers_destinations(self, traveler):

        return traveler.destinations.all()


class DetailsPageVisitedCounterMixin:

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count = F('view_count') + 1
        obj.save(update_fields=['view_count'])

        obj.refresh_from_db()

        return obj

