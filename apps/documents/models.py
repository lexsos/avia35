from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class DocumentType(models.Model):

    title = models.CharField(
        verbose_name=_('doctype title'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('doctype description'),
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('documents types')
        verbose_name = _('document type')
        ordering = ['title']


class DocumentCategory(Publication):

    title = models.CharField(
        verbose_name=_('document category title'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('document category description'),
        blank=True,
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('document category items')
        verbose_name = _('document category item')
        ordering = ['title']


class Document(Publication):

    doc_type = models.ForeignKey(
        DocumentType,
        verbose_name=_('document type'),
    )
    category = models.ForeignKey(
        DocumentCategory,
        verbose_name=_('document category item'),

    )
    title = models.CharField(
        verbose_name=_('document title'),
        max_length=255,
    )
    document = models.FileField(
        upload_to='documents',
        verbose_name=_('document file'),
    )

    def get_size_text(self):
        if self.document is None:
            return u'{0} {1}'.format(0, _('b'))
        size = self.document.size
        unit = _('b')

        if size > 1024:
            size = size/1024.0
            unit = _('Kb')
        if size > 1024:
            size = size/1024.0
            unit = _('Mb')
        if size > 1024:
            size = size/1024.0
            unit = _('Gb')

        return u'{0:0.1f} {1}'.format(size, unit)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('documents')
        verbose_name = _('document')
        ordering = ['-weight', 'pub_date_start']
