from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import DocumentCategory


urlpatterns = patterns('',
    url(
        r'^$',
        PublicationListView.as_view(
            model=DocumentCategory,
            template_name = 'documents/document_list.html'
        ),
        name='document_list',
    ),
)
