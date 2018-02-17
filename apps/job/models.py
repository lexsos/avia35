from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import Publication


class Vacancy(Publication):
    title = models.CharField(verbose_name=_('vacancy title'), max_length=255)
    description = models.TextField(verbose_name=_('vacancy description'), blank=True)
    requirements = models.TextField(verbose_name=_('vacancy requirements'), blank=True)
    schedule = models.CharField(verbose_name=_('vacancy schedule'), max_length=255, blank=True)
    payment = models.CharField(verbose_name=_('vacancy payment'), max_length=255, blank=True)
    contacts = models.CharField(verbose_name=_('vacancy contacts'), max_length=255, blank=True)
    additionally = models.TextField(verbose_name=_('vacancy additionally'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('vacances')
        verbose_name = _('vacancy')
        ordering = ['-weight', '-pub_date_start']


class VacancyResponse(models.Model):

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name=_('vacancy'))
    fio = models.CharField(verbose_name=_('response fio'), max_length=255)
    phone = models.CharField(verbose_name=_('response phone'), max_length=255)
    about_self = models.TextField(verbose_name=_('vacancy description'), blank=True)
    summary = models.FileField(upload_to='job', verbose_name=_('response summary'), blank=True)
    create_date = models.DateTimeField(auto_now=True, verbose_name=_('response date'))

    def __str__(self):
        return '{}:{}'.format(self.vacancy.title, self.fio)

    class Meta:
        verbose_name_plural = _('vacances responses')
        verbose_name = _('vacancy response')
        ordering = ['-create_date']


class Note(Publication):

    content = models.TextField(verbose_name=_('note content'))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = _('notes items')
        verbose_name = _('note item')
        ordering = ['-weight', 'content']
