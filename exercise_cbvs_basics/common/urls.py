from django.urls import path
from common.views import BasicView, HomeView, DestinationsStatusView, AgeCheckRedirectView, WelcomeView

urlpatterns = [
    path('', BasicView.as_view(), name='basic_view'),
    path('home/', HomeView.as_view(), name='home'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('status/', DestinationsStatusView.as_view(), name='status'),
    path('age-check/', AgeCheckRedirectView.as_view(), name='age-check')

]