from django.conf.urls import url

from helpers.views import PublicationDetailView
from schedule.models import Flight
from schedule.views import FlightListView


urlpatterns = [
    url(r'^$', FlightListView.as_view(), name='schedule_list'),
    url(r'^agents/(?P<pk>\d+)/$',
        PublicationDetailView.as_view(model=Flight, template_name='schedule/flight_agents.html'),
        name='schedule_flight_agents'),
]
