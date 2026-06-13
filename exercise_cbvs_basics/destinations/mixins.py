from destinations.models import Destination


class DestinationAvailabilityMixin:

    def get_available_destinations(self):
        return Destination.objects.filter(is_available=True)