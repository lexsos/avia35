from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class Contact(Publication):
    title = models.CharField(
        verbose_name=_('contact title'),
        max_length=255,
    )
    content = models.TextField(
        verbose_name=_('contact content'),
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('contacts')
        verbose_name = _('contact')
        ordering = ['-weight', '-pub_date_start']
