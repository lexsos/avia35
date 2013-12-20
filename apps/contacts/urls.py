from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import Contact


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(model=Contact),
        name='contact_list',
    ),
)
