from django.urls import path

from destinations.views import DestinationCreateView, DestinationDeleteView, DestinationsList

urlpatterns = [
    path('destination-create/', DestinationCreateView.as_view(), name ='destination-create'),
    path('destinations-list/', DestinationsList.as_view(), name = 'destinations-list'),
    path('<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination-delete')

]