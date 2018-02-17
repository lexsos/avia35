from django.conf.urls import url

from helpers.views import PublicationListView, PublicationDetailView
from news.models import News


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=News, paginate_by=3), name='news_list'),
    url(r'^(?P<pk>\d+)/$', PublicationDetailView.as_view(model=News), name='news_detail'),
]
