from django.db import models
from helpers.models import Publication


class Contact(Publication):
    title = models.CharField(verbose_name='заголовок', max_length=255)
    content = models.TextField(verbose_name='содержимое')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'контакты'
        verbose_name = 'контакт'
        ordering = ['-weight', '-pub_date_start']
