from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from dj_mixin.publications.views import PublicationListView

from .models import Document, DocumentCategory, DocumentCounter


class DocumentListView(PublicationListView):

    model = DocumentCategory
    template_name = 'documents/document_list.html'


class DocumentCounterRedirectView(RedirectView):

    permanent = False

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get_redirect_url(self, pk):

        qs = Document.objects.published()
        document = get_object_or_404(qs, pk=pk)

        qs_category = DocumentCategory.objects.published()
        get_object_or_404(qs_category, pk=document.category.pk)

        counter = DocumentCounter(
            document = document,
            user_agent= self.request.META['HTTP_USER_AGENT'],
            client_ip = self.get_client_ip(),
        )
        counter.save()
        return document.document.url
