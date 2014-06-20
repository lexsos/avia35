from django.conf.urls import patterns, url

from .views import FAQListView


urlpatterns = patterns(
    '',
    url(
        r'^$',
        FAQListView.as_view(),
        name='faq_list',
    ),
)
