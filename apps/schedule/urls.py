from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView, PublicationDetailView

from .models import Flight


urlpatterns = patterns('',
    url(r'^$',
        PublicationListView.as_view(model=Flight),
        name='schedule_list'
    ),
    url(r'^agents/(?P<pk>\d+)/$',
        PublicationDetailView.as_view(model=Flight, template_name='schedule/flight_agents.html'),
        name='schedule_flight_agents',
    ),
)

