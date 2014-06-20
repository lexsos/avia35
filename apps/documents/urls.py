from django.conf.urls import patterns, url

from .views import DocumentCounterRedirectView, DocumentListView


urlpatterns = patterns(
    '',
    url(
        r'^$',
        DocumentListView.as_view(),
        name='document_list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        DocumentCounterRedirectView.as_view(),
        name='document_counter',
    ),
)
