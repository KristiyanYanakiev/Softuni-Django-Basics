from datetime import timedelta

from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models.aggregates import Avg
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, ListView, DetailView, TemplateView

from common.mixins import AgeRestrictionMixin, RecentObjectsMixin
from destinations.forms import DestinationForm
from destinations.mixins import DestinationAvailabilityMixin
from destinations.models import Destination


# Create your views here.
class DestinationCreateView(CreateView):
    template_name = 'destinations/destination_form.html'
    form_class = DestinationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Destination successfully created")
        return super().form_valid(form)


class DestinationDeleteView(DeleteView):
    model = Destination
    success_url = reverse_lazy('home')
    template_name = 'destinations/destination_delete_confirmation.html'


class DestinationsList(ListView):
    template_name = 'destinations/destination_list.html'
    model = Destination


class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'destinations/detail.html'
    context_object_name = 'destination'

    def get_queryset(self):
        return (Destination.objects
                .prefetch_related('reviews', 'travelers')
                .annotate(avg_rating=Avg('reviews__rating')))


class DestinationListView(AgeRestrictionMixin, ListView):
    context_object_name = 'destinations'
    # template_name = 'destinations/list.html'
    model = Destination
    paginate_by = 3



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     total_available_destinations = Destination.objects.filter(is_available=True).count()
    #
    #     context['total_available_destinations'] = total_available_destinations
    #
    #
    #     return context

    def get_template_names(self):
        traveler_country = self.request.GET.get('traveler_country')
        if traveler_country:
            if traveler_country.upper() in ['BG', 'GR', 'TR']:
                print("--- DEBUG: Condition Met! Attempting Balkan Template ---")
                return ['destinations/balkan_list.html']
        print("--- DEBUG: Condition Failed. Falling back to default list ---")
        return ['destinations/list.html']


class DestinationByCountryListView(DestinationAvailabilityMixin, ListView):
    model = Destination
    template_name = 'destinations/destinations_by_country.html'
    context_object_name = 'destinations'

    def get_queryset(self):

        country = self.request.GET.get('country')
        qs = self.get_available_destinations()
        if country:
            qs = qs.filter(country=country)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country'] = self.request.GET.get('country')
        print(context)
        return context


class RecentDestinationsView(ListView):
    model = Destination
    template_name = 'destinations/recent.html'
    context_object_name = 'recent_destinations'

    def get_queryset(self):
        now = timezone.now()
        seven_days_ago = now - timedelta(days=7)

        return Destination.objects.filter(updated_at__gte=seven_days_ago).order_by('-updated_at')


class FeaturedDestinationListView(DestinationListView):
    def get_queryset(self):
        return Destination.objects.order_by('reviews__rating')[:2]


class DestinationJSONTestView(DetailView):
    model = Destination

    def render_to_response(self, context, **response_kwargs):
        destination = context['object']

        data = {
            "pk": destination.pk,
            "name": destination.name,
            "price": float(destination.price),
            "is_available": destination.is_available,
        }

        # 3. Return a JsonResponse instead of rendering an HTML template
        return JsonResponse(data)


class DestinationsOffers(TemplateView):

    template_name = 'destinations/offers.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs
                                           )
        context['offers'] = Destination.objects.annotate(
            avg_rating=Avg('reviews__rating')
        ).filter(
            avg_rating__gte=4.50,
            is_available=True
        ).order_by('-avg_rating')


        return context


class DestinationsListByPrice(DestinationListView):

    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('price')
        if query:
            qs = qs.filter(price__lte=query)

        return qs

    def get_paginate_by(self, queryset):

        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_pages'] = context['page_obj'].paginator.num_pages


        return context
