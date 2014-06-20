from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationDetailView

from .models import Flight
from .views import FlightListView


urlpatterns = patterns(
    '',
    url(
        r'^$',
        FlightListView.as_view(),
        name='schedule_list',
    ),
    url(
        r'^agents/(?P<pk>\d+)/$',
        PublicationDetailView.as_view(
            model=Flight,
            template_name='schedule/flight_agents.html',
        ),
        name='schedule_flight_agents',
    ),
)
