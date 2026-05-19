from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from destinations.models import Destination
from reviews.forms import ReviewForm


# Create your views here.
class AddReview(CreateView):
    template_name = 'reviews/review_form.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        destination = get_object_or_404(Destination, pk=self.kwargs['destination_pk'] )

        context["destination"] = destination
        context["message"] = f"You are adding a review for {destination.name}"

        return context

    def form_valid(self, form):
        messages.success(self.request, 'Review successfully submitted')

        return super().form_valid(form)



