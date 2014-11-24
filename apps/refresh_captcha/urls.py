from django.conf.urls import patterns, url

from .views import refresh_captcha


urlpatterns = patterns(
    '',
    url(
        r'^$',
        refresh_captcha,
        name='refresh_captcha',
    ),
)
