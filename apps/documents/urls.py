from django.conf.urls import url

from documents.views import DocumentCounterRedirectView, DocumentListView


urlpatterns = [
    url(r'^$', DocumentListView.as_view(), name='document_list'),
    url(r'^(?P<pk>\d+)/$', DocumentCounterRedirectView.as_view(), name='document_counter'),
]
