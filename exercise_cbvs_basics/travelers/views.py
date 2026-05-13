from django.shortcuts import render
from django.views.generic import FormView, CreateView, RedirectView

from travelers.forms import TravelerForm
from travelers.models import Traveler


# Create your views here.
class TravelerCreateView(CreateView):
    template_name = 'travelers/traveler_form.html'
    model = Traveler
    form_class = TravelerForm


class TravelerRegistrationRedirectView(RedirectView):
    pattern_name = 'travelers:traveler-registration'
