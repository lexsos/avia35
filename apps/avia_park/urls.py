from django.conf.urls import url

from helpers.views import PublicationListView, PublicationDetailView
from avia_park.models import Craft


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Craft), name='avia_park_list'),
    url(r'^(?P<slug>[-_\w]+)/$', PublicationDetailView.as_view(model=Craft), name='avia_park_detail'),
]

