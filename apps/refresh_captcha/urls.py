from django.conf.urls import url

from refresh_captcha.views import refresh_captcha


urlpatterns = [
    url(r'^$', refresh_captcha, name='refresh_captcha'),
]
