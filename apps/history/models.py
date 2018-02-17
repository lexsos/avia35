from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import Publication


LEFT_SIDE = 'LF'
RIGHT_SIDE = 'RG'

SIDE_CHOICES = (
    (LEFT_SIDE, _('left')),
    (RIGHT_SIDE, _('right')),
)

IMG_WIDTH = 'WD'
IMG_HEIGHT = 'HG'

IMG_ADJUSTMENT_CHOICES = (
    (IMG_WIDTH, _('by width')),
    (IMG_HEIGHT, _('by height')),
)


class ContentBlock(Publication):

    name = models.CharField(verbose_name=_('block name'), max_length=255)
    content_rich = models.TextField(verbose_name=_('rich content'), blank=True)
    content_plane = models.TextField(verbose_name=_('plane content'), blank=True)

    def get_left(self):
        return self.sidecontent_set.published().filter(side=LEFT_SIDE)

    def get_right(self):
        return self.sidecontent_set.published().filter(side=RIGHT_SIDE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('content block item')
        verbose_name_plural = _('content block items')
        ordering = ['-weight', '-pub_date_start']


class SideContent(Publication):

    name = models.CharField(verbose_name=_('content name'), max_length=255)
    content_block = models.ForeignKey(ContentBlock, on_delete=models.CASCADE, verbose_name=_('content block item'))
    content_rich = models.TextField(verbose_name=_('rich content'), blank=True)
    content_plane = models.TextField(verbose_name=_('plane content'), blank=True)
    image = models.ImageField(verbose_name=_('image content'), upload_to='history', blank=True, null=True)
    side = models.CharField(verbose_name=_('content side'), max_length=255, choices=SIDE_CHOICES)
    detail_content_rich = models.TextField(verbose_name=_('detail rich content'), blank=True)
    detail_content_plane = models.TextField(verbose_name=_('detail plane content'), blank=True)
    detail_img_adjustment = models.CharField(
        verbose_name=_('detail image adjustment'), max_length=255, choices=IMG_ADJUSTMENT_CHOICES, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('side content item')
        verbose_name_plural = _('side content items')
        ordering = ['content_block', 'side', '-weight', '-pub_date_start']
