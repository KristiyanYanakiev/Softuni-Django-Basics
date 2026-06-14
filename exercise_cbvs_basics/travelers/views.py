from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, RedirectView, UpdateView, DetailView, ListView

from travelers.forms import TravelerForm
from travelers.mixins import TravelerActivityMixin, DetailsPageVisitedCounterMixin
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


class TravelerDetailView(DetailsPageVisitedCounterMixin, TravelerActivityMixin, DetailView):
    model = Traveler
    template_name = 'travelers/detail.html'
    context_object_name = 'traveler'

    def get_context_data(self, **kwargs):
        traveler = self.object
        context = super().get_context_data(**kwargs)

        context["reviews"] = self.get_travelers_reviews(traveler)
        context["destinations"] = self.get_travelers_destinations(traveler)
        print(context['reviews'])
        print(context['destinations'])

        return context


class TravelerListView(ListView):
    model = Traveler
    template_name = 'travelers/list.html'
    context_object_name = 'travelers'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            queryset = Traveler.objects.filter(name__icontains=query).filter(age__gte=21)
        else:
            queryset = Traveler.objects.filter(age__gte=21)


        return queryset

