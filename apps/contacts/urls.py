from django.conf.urls import url

from helpers.views import PublicationListView
from contacts.models import Contact


urlpatterns = [
    url(r'^$', PublicationListView.as_view(model=Contact), name='contact_list'),
]
