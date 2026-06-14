from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from common.mixins import AgeRestrictionMixin, RecentObjectsMixin, CustomAccessMixin
from destinations.models import Destination
from reviews.forms import ReviewForm
from reviews.models import Review


# Create your views here.
# @method_decorator(login_required(login_url='home'), name='dispatch')

class AddReview(LoginRequiredMixin, CreateView):
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



class ReviewListView(AgeRestrictionMixin, CustomAccessMixin, ListView):
    # http_method_names = ['get']
    login_url = 'home'
    model = Review
    template_name = 'reviews/list.html'
    context_object_name = 'reviews'

    def get_queryset(self):

        qs = Review.objects.filter(is_verified=True).order_by('pk')
        review_type = self.request.GET.get('review_type')

        if review_type:
            qs = qs.filter(review_type=review_type)


        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_number = self.request.GET.get('page', 1)
        context['page_number'] = page_number

        return context

    def get_paginate_by(self, queryset):
        per_page = self.request.GET.get('per_page', 1)

        return per_page

    # def render_to_response(self, context, **response_kwargs):
    #
    #     response = super().render_to_response(context, **response_kwargs)
    #     print("Here is my context:")
    #     print(context)
    #
    #     return response


class VerifiedReviewListView(ReviewListView):
    def get_queryset(self):

        return super().get_queryset().filter(is_verified=True)





