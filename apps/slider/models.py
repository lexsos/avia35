from django.db import models
from django.utils.translation import ugettext_lazy as _


class Slide(models.Model):
    title = models.TextField(
        verbose_name=_('slide title'),
        help_text=_('text on slide'),
    )
    image = models.ImageField(
        verbose_name=_('slide image'),
        help_text=_('image of slide'),
        upload_to = 'slider',
    )
    weight = models.IntegerField(
        verbose_name=_('weight'),
        default=0,
        help_text=_('determine the order of slides'),
    )
    enabled = models.BooleanField(
        verbose_name=_('enabled'),
        default=True,
        help_text=_('if set, then slide will show'),
    )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-weight']
        verbose_name_plural = _('slides')
        verbose_name = _('slide')
