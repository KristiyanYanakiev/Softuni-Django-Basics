from django.urls import path

from destinations.views import DestinationCreateView, DestinationDeleteView, DestinationsList, DestinationDetailView, \
    DestinationListView, DestinationByCountryListView, RecentDestinationsView, DestinationJSONTestView, \
    DestinationsOffers, DestinationsListByPrice

app_name = 'destinations'
urlpatterns = [
    path('destination-create/', DestinationCreateView.as_view(), name ='destination-create'),
    path('destinations-list/', DestinationsList.as_view(), name = 'destinations-list'),
    path('<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination-delete'),
    path('<int:pk>/details/', DestinationDetailView.as_view(), name='details'),
    path('list/', DestinationListView.as_view(), name='list'),
    path('list-by-country/', DestinationByCountryListView.as_view(), name='list-by-country'),
    path('recent-list/', RecentDestinationsView.as_view(), name='recent-list'),
    path('best-list/', DestinationListView.as_view(), name='best-list'),
    path('<int:pk>/json-test/', DestinationJSONTestView.as_view(), name='json-test'),
    path('offers/', DestinationsOffers.as_view(), name='offers'),
    path('list-by-price/', DestinationsListByPrice.as_view(), name='list-by-price')

]