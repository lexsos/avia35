from django.conf.urls import patterns, url
from dj_mixin.publications.views import (
    PublicationListView,
    PublicationDetailView,
)

from .models import ContentBlock, SideContent


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(model=ContentBlock),
        name='history_list',
    ),
    url(
        r'^img/(?P<pk>\d+)/$',
        PublicationDetailView.as_view(model=SideContent),
        name='history_img_detail',
    ),
)
