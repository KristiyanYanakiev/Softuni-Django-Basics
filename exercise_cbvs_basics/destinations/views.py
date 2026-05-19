from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

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



