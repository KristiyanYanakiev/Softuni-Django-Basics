from django.urls import path

from travelers.views import TravelerCreateView, TravelerRegistrationRedirectView, TravelerCreateViewFormView

app_name = 'travelers'

urlpatterns = [
    path('traveler-registration/', TravelerCreateView.as_view(), name='traveler-registration' ),
    path('traveler-registration-form-view/', TravelerCreateViewFormView.as_view()),
    path('redirect-registration/', TravelerRegistrationRedirectView.as_view() )
]