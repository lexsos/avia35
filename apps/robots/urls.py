from django.conf.urls import url

from robots.views import robots_txt


urlpatterns = [
    url(r'^$', robots_txt, name='robots_txt'),
]
