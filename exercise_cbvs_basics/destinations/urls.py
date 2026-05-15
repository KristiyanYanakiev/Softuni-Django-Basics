from django.urls import path

from destinations.views import DestinationCreateView, DestinationDeleteView

urlpatterns = [
    path('destination-create/', DestinationCreateView.as_view(), name ='destination-create'),
    path('<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination-delete')

]