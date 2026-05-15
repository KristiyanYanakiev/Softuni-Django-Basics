from django.urls import path

from travelers.views import TravelerCreateView, TravelerRegistrationRedirectView, TravelerCreateViewFormView, \
    TravelerUpdate

app_name = 'travelers'

urlpatterns = [
    path('traveler-registration/', TravelerCreateView.as_view(), name='traveler-registration' ),
    path('traveler-registration-form-view/', TravelerCreateViewFormView.as_view()),
    path('traveler/<int:pk>/edit/', TravelerUpdate.as_view(), name='traveler-edit'),
    path('redirect-registration/', TravelerRegistrationRedirectView.as_view() )
]