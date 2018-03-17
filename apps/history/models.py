from django.db import models
from helpers.models import Publication


LEFT_SIDE = 'LF'
RIGHT_SIDE = 'RG'

SIDE_CHOICES = ((LEFT_SIDE, 'лево'), (RIGHT_SIDE, 'право'))

IMG_WIDTH = 'WD'
IMG_HEIGHT = 'HG'

IMG_ADJUSTMENT_CHOICES = ((IMG_WIDTH, 'по ширене'), (IMG_HEIGHT, 'по высоте'))


class ContentBlock(Publication):

    name = models.CharField(verbose_name='имя блока', max_length=255)
    content_rich = models.TextField(verbose_name='содержимое с оформлением', blank=True)
    content_plane = models.TextField(verbose_name='содержимое без оформления', blank=True)

    def get_left(self):
        return self.sidecontent_set.published().filter(side=LEFT_SIDE)

    def get_right(self):
        return self.sidecontent_set.published().filter(side=RIGHT_SIDE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блок содержимого'
        verbose_name_plural = 'блоки содержимого'
        ordering = ['-weight', '-pub_date_start']


class SideContent(Publication):

    name = models.CharField(verbose_name='имя', max_length=255)
    content_block = models.ForeignKey(ContentBlock, on_delete=models.CASCADE, verbose_name='блок содержимого')
    content_rich = models.TextField(verbose_name='содержимое с оформлением', blank=True)
    content_plane = models.TextField(verbose_name='содержимое без оформления', blank=True)
    image = models.ImageField(verbose_name='изображение', upload_to='history', blank=True, null=True)
    side = models.CharField(verbose_name='сторона', max_length=255, choices=SIDE_CHOICES)
    detail_content_rich = models.TextField(verbose_name='содержимое с оформлением', blank=True)
    detail_content_plane = models.TextField(verbose_name='содержимое без оформления', blank=True)
    detail_img_adjustment = models.CharField(
        verbose_name='подгонка изображения', max_length=255, choices=IMG_ADJUSTMENT_CHOICES, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'содержимое стороны'
        verbose_name_plural = 'содержимое сторон'
        ordering = ['content_block', 'side', '-weight', '-pub_date_start']
