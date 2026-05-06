from datetime import timezone

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View
from django.views.generic import TemplateView, RedirectView


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

class HomeRedirectView(RedirectView):
    pattern_name = 'travelers:traveler-registration'