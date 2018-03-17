from django.db import models
from django.contrib.sites.models import Site

from helpers.models import Publication


class RobotData(Publication):

    description = models.CharField(verbose_name='описание', max_length=255)
    content = models.TextField(verbose_name='данные робота')
    site = models.ForeignKey(Site, verbose_name='сайт', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'параметры роботов'
        verbose_name = 'параметры робота'
        ordering = ['-weight', '-pub_date_start']
