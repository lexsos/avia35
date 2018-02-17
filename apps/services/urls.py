from django.conf.urls import url

from helpers.views import PublicationDetailView
from services.models import ServiceType


urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', PublicationDetailView.as_view(model=ServiceType), name='services_list'),
]
