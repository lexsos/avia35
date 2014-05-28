from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .views import FAQListView


urlpatterns = patterns('',
    url(
        r'^$',
        FAQListView.as_view(),
        name='faq_list',
    ),
)
