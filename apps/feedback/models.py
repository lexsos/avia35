from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):

    fio = models.CharField(verbose_name=_('user fio'), max_length=255)
    contact = models.CharField(verbose_name=_('user contact'), max_length=255)
    content = models.TextField(verbose_name=_('question content'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('create date'))
    answered = models.BooleanField(default=False, verbose_name=_('answered'))

    def __str__(self):
        return '{}:{}'.format(self.fio, self.contact)

    class Meta:
        verbose_name_plural = _('questions items')
        verbose_name = _('question item')
        ordering = ['-create_date']
