from django.db import models
from django.utils import timezone

from helpers.managers import PublicationManager


class Publication(models.Model):

    """Abstract model fot publication like objects."""

    enabled = models.BooleanField(verbose_name='включено', default=True, db_index=True, help_text='показать/скрыть')
    pub_date_start = models.DateTimeField(
        verbose_name='дата начала публикации', default=timezone.now, db_index=True,
        help_text='Будет отображаться начиная с указанной даты')
    pub_date_end = models.DateTimeField(
        verbose_name='дата конца публикации', null=True, blank=True, db_index=True,
        help_text='Будет скрыто начиная с указанной даты')
    weight = models.PositiveIntegerField(
        verbose_name='вес', db_index=True, default=0, help_text='Запись с большим весом будет первой')

    objects = PublicationManager()

    class Meta:
        abstract = True
        ordering = ['-weight', '-pub_date_start']
