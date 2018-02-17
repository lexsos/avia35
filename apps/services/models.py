from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import Publication


class ServiceType(Publication):

    title = models.CharField(verbose_name=_('service type title'), max_length=255)
    slug = models.CharField(verbose_name=_('service type slug'), max_length=255, unique=True)

    class Meta:
        verbose_name_plural = _('services type items')
        verbose_name = _('service type item')
        ordering = ['-weight', 'title']

    def __str__(self):
        return self.title


class Service(Publication):

    service_type = models.ForeignKey(ServiceType, verbose_name=_('service type'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('service title'), max_length=255)
    description = models.TextField(verbose_name=_('service description'), blank=True)

    class Meta:
        verbose_name_plural = _('services items')
        verbose_name = _('service item')
        ordering = ['-weight', 'title']

    def __str__(self):
        return '{}:{}'.format(self.service_type.title, self.title)


class ServiceParametr(models.Model):

    service = models.ForeignKey(Service, verbose_name=_('service item'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('service parametr title'), max_length=255)
    content = models.TextField(verbose_name=_('service parametr content'))

    class Meta:
        verbose_name_plural = _('services parametrs items')
        verbose_name = _('service parametr item')
        ordering = ['service', 'title']

    def __str__(self):
        return '{}:{}'.format(self.service.title, self.title)


class ServiceImage(models.Model):

    service = models.ForeignKey(Service, verbose_name=_('service item'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('service image title'), max_length=255)
    image = models.ImageField(verbose_name=_('service image'), upload_to='services')

    class Meta:
        verbose_name_plural = _('services images items')
        verbose_name = _('service image item')
        ordering = ['service', 'title']

    def __str__(self):
        return '{}:{}'.format(self.service.title, self.title)
