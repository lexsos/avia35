from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import Vacancy


urlpatterns = patterns('',
    url(r'^$', PublicationListView.as_view(model=Vacancy), name='job_list'),
)

