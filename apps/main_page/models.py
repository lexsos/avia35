from django.db import models
from helpers.models import Publication


class Content(Publication):

    title = models.CharField(verbose_name='название', max_length=255)
    content_rich = models.TextField(verbose_name='содержимое с оформлением', blank=True)
    content_plane = models.TextField(verbose_name='содержимое без оформления', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'содержимое'
        verbose_name = 'содержимое'
        ordering = ['-weight', '-pub_date_start']
