from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class News(Publication):
    title = models.CharField(
        verbose_name=_('news title'),
        max_length=255,
    )
    preview = models.TextField(
        verbose_name=_('news preview'),
    )
    content = models.TextField(
        verbose_name=_('news content'),
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_('news image'),
        upload_to='news',
    )

    def get_content(self):
        if self.content:
            return self.content
        return self.preview

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('news items')
        verbose_name = _('news item')
        ordering = ['-weight', '-pub_date_start']
