from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationDetailView

from .models import ServiceType


urlpatterns = patterns('',
    url(
        r'^(?P<slug>[-_\w]+)/$',
        PublicationDetailView.as_view(model=ServiceType),
        name='services_list',
    ),
)
