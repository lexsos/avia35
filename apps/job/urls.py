from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import Vacancy
from .views import AddResponse


urlpatterns = patterns('',
    url(r'^$', PublicationListView.as_view(model=Vacancy), name='job_list'),
    url(r'(?P<pk>\d+)/$', AddResponse.as_view(), name='job_add_response'),
)

