from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView
from django.views.generic import TemplateView

from .models import Vacancy
from .views import AddResponse, VacancyListView


urlpatterns = patterns('',
    url(
        r'^$',
        VacancyListView.as_view(),
        name='job_list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        AddResponse.as_view(),
        name='job_add_response',
    ),
    url(
        r'^success/$',
        TemplateView.as_view(template_name="job/response_success.html"),
        name='job_response_success',
    ),
)
