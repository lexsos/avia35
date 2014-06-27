from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class Agent(models.Model):

    title = models.CharField(
        verbose_name=_('agent title'),
        max_length=255,
    )
    url = models.URLField(verbose_name=_('agent url'))
    image = models.ImageField(
        verbose_name=_('agent logo'),
        upload_to='schedule',
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('agents items')
        verbose_name = _('agent item')
        ordering = ['title']


class Flight(Publication):

    direction = models.CharField(
        verbose_name=_('flight direction'),
        max_length=255,
    )
    flight_no = models.CharField(
        verbose_name=_('flight number'),
        max_length=255,
        blank=True,
    )
    departure = models.TextField(
        verbose_name=_('flight departure'),
    )
    arrival = models.TextField(
        verbose_name=_('flight arrival'),
    )
    order = models.TextField(
        verbose_name=_('flight order'),
        blank=True,
    )
    agents = models.ManyToManyField(
        Agent,
        verbose_name=_('flight agents'),
        blank=True,
    )

    def __unicode__(self):
        return self.direction

    class Meta:
        verbose_name_plural = _('flights items')
        verbose_name = _('flight item')
        ordering = ['-weight', 'direction']


class Note(Publication):

    content = models.TextField(
        verbose_name=_('note content'),
    )

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name_plural = _('notes items')
        verbose_name = _('note item')
        ordering = ['-weight', 'content']


class PaymentBanner(Publication):

    image = models.ImageField(
        verbose_name=_('payment image'),
        upload_to='schedule',
    )
    title = models.CharField(
        verbose_name=_('payment title'),
        max_length=255,
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('payment banners items')
        verbose_name = _('payment banner item')
        ordering = ['-weight', 'title']
