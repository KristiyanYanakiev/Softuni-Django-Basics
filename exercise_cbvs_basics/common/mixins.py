from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from travelers.models import Traveler


class AgeRestrictionMixin:
    def dispatch(self, request, *args, **kwargs):
        traveler_id = request.GET.get('pk')
        if traveler_id:
            traveler = get_object_or_404(Traveler, pk=traveler_id)

            if traveler.age < 21:
                return HttpResponseRedirect(reverse('welcome'))

        return super().dispatch(request, *args, **kwargs)


class RecentObjectsMixin:
    limit = 1
    def get_queryset(self):
        qs = super().get_queryset()

        return qs.order_by('-created_at')[:self.limit]


