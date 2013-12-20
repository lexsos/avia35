from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView, PublicationDetailView

from .models import Craft


urlpatterns = patterns('',
    url(r'^$',
        PublicationListView.as_view(model=Craft),
        name='avia_park_list',
    ),
    url(r'^(?P<slug>[-_\w]+)/$',
        PublicationDetailView.as_view(model=Craft),
        name='avia_park_detail',
    ),
)

