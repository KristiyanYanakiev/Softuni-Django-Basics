from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from destinations.models import Destination
from reviews.forms import ReviewForm
from reviews.models import Review


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


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/list.html'
    context_object_name = 'reviews'
    paginate_by = 1

    def get_queryset(self):

        qs = Review.objects.filter(is_verified=True).order_by('created_at')

        review_type = self.request.GET.get('review_type')

        if review_type:
            qs = qs.filter(review_type=review_type)


        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_number'] = page_number

        return context






