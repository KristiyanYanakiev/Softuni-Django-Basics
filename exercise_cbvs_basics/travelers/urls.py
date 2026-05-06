from django.urls import path

from travelers.views import TravelerCreateView

app_name = 'travelers'

urlpatterns = [
    path('traveler-registration/', TravelerCreateView.as_view(), name='traveler-registration' ),
]