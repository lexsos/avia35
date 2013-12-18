from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import Document


urlpatterns = patterns('',
    url(r'^$', PublicationListView.as_view(model=Document), name='document_list'),
)

