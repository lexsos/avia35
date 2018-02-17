from django.conf.urls import url
from helpers.views import PublicationListView

from main_page.models import Content


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Content), name='main_page'),
]
