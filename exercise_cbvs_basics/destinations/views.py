from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.db.models.aggregates import Avg
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView

from destinations.forms import DestinationForm
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


class DestinationListView(ListView):
    context_object_name = 'destinations'
    # template_name = 'destinations/list.html'
    model = Destination
    paginate_by = 1


    # def get_queryset(self):
    #     return Destination.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_available_destinations = Destination.objects.filter(is_available=True).count()

        context['total_available_destinations'] = total_available_destinations


        return context

    def get_template_names(self):
        traveler_country = self.request.GET.get('traveler_country')
        if traveler_country:
            if traveler_country.upper() in ['BG', 'GR', 'TR']:
                print("--- DEBUG: Condition Met! Attempting Balkan Template ---")
                return ['destinations/balkan_list.html']
        print("--- DEBUG: Condition Failed. Falling back to default list ---")
        return ['destinations/list.html']
