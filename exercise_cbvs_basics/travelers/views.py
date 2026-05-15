from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, RedirectView, UpdateView

from travelers.forms import TravelerForm
from travelers.models import Traveler


# Create your views here.
class TravelerCreateView(CreateView):
    template_name = 'travelers/traveler_form.html'
    form_class = TravelerForm
    success_url = reverse_lazy('home')


class TravelerCreateViewFormView(FormView):
    template_name = 'travelers/traveler_form.html'
    form_class = TravelerForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Traveler successfully created")
        return super().form_valid(form)

class TravelerRegistrationRedirectView(RedirectView):
    pattern_name = 'travelers:traveler-registration'


class TravelerUpdate(UpdateView):
    form_class = TravelerForm
    model = Traveler
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        print('Object updated')
        return super().form_valid(form)
