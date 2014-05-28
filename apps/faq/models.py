from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class FrequentlyQuestion(Publication):

    title = models.CharField(
        verbose_name=_('question title'),
        max_length=255,
    )
    question = models.TextField(
        verbose_name=_('question'),
    )
    answer = models.TextField(
        verbose_name=_('answer'),
    )

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name_plural = _('frequently questions items')
        verbose_name = _('frequently question item')
        ordering = ['-weight', '-pub_date_start']
