from django.shortcuts import get_object_or_404

from helpers.views import PublicationDetailView
from history.models import SideContent, ContentBlock


class ImgDetailView(PublicationDetailView):

    model = SideContent

    def get_queryset(self):
        queryset = super(ImgDetailView, self).get_queryset()
        queryset = queryset.exclude(detail_img_adjustment='')
        return queryset

    def get_object(self, queryset=None):
        side = super(ImgDetailView, self).get_object(queryset)

        qs_block = ContentBlock.objects.published()
        get_object_or_404(qs_block, pk=side.content_block.pk)

        return side
