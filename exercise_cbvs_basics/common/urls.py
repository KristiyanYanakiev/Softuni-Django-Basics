from django.urls import path
from common.views import BasicView

urlpatterns = [
    path('', BasicView.as_view(), name='basic_view')
]