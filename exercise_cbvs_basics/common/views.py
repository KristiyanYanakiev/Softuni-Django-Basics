from datetime import timezone

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView

from destinations.models import Destination
from travelers.models import Traveler


# Create your views here.
class BasicView(View):
    def get(self, request: HttpRequest):
        return HttpResponse('Welcome to Traveler Management')

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Post was called")


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'message': 'Hello world!',
            'current_time': str(now())

        })

        return super().get_context_data(**kwargs)


class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class HomeRedirectView(RedirectView):
    pattern_name = 'travelers:traveler-registration'


class DestinationsStatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):

        if Destination.objects.exists():
            kwargs['status'] = 'Pack your bags!'
        else:
            kwargs['status'] = 'No destinations available at the moment.'

        return super().get_context_data(**kwargs)


class AgeCheckRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):

        pk = self.request.GET.get('traveler_pk')
        traveler = get_object_or_404(Traveler, pk=pk)

        if traveler.age >= 21:
            return reverse_lazy('home')

        return reverse_lazy('welcome')
