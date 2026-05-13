from django.urls import path

from travelers.views import TravelerCreateView, TravelerRegistrationRedirectView

app_name = 'travelers'

urlpatterns = [
    path('traveler-registration/', TravelerCreateView.as_view(), name='traveler-registration' ),
    path('redirect-registration/', TravelerRegistrationRedirectView.as_view() )
]