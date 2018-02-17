from django.conf.urls import url

from helpers.views import PublicationListView
from history.models import ContentBlock
from history.views import ImgDetailView


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=ContentBlock), name='history_list'),
    url(r'^img/(?P<pk>\d+)/$', ImgDetailView.as_view(), name='history_img_detail'),
]
