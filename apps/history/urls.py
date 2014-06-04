from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import ContentBlock
from .views import ImgDetailView


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(model=ContentBlock),
        name='history_list',
    ),
    url(
        r'^img/(?P<pk>\d+)/$',
        ImgDetailView.as_view(),
        name='history_img_detail',
    ),
)
