from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import ContentBlock


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(model=ContentBlock),
        name='history_list',
    ),
)
