from django.urls import path
from common.views import BasicView, HomeView

urlpatterns = [
    path('', BasicView.as_view(), name='basic_view'),
    path('home/', HomeView.as_view(), name='home')

]