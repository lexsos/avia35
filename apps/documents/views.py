from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from dj_mixin.publications.views import PublicationListView

from .models import Document, DocumentCategory


class DocumentListView(PublicationListView):

    model = DocumentCategory
    template_name = 'documents/document_list.html'


class DocumentCounterRedirectView(RedirectView):

    permanent = False

    def get_redirect_url(self, pk):
        document = get_object_or_404(Document, pk=pk)
        return document.document.url
