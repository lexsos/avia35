from django.conf.urls import patterns, url
from dj_mixin.publications.views import PublicationListView

from .models import RobotData
from .views import robots_txt


urlpatterns = patterns('',
    url(r'^$', robots_txt, name='robots_txt'),
)
