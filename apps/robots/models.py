from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from dj_mixin.publications.models import Publication


class RobotData(Publication):

    description = models.CharField(
        verbose_name=_('description'),
        max_length=255,
    )
    content = models.TextField(
        verbose_name=_('robot content'),
    )
    site = models.ForeignKey(
        Site,
        verbose_name=_(u'site'),
    )

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = _('robot data items')
        verbose_name = _('robot data item')
        ordering = ['-weight', '-pub_date_start']