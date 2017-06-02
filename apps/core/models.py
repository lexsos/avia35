from django.db import models
from django.utils.translation import ugettext_lazy as _


class PageContent(models.Model):

    MAIN, SCHEDULE, SERVICES, NEWS_LIST, NEWS_DETAIL, DOCUMENTS, CONTACTS, FAQ, JOB = (
        'main_page', 'schedule_list', 'services_list', 'news_list', 'news_detail', 'document_list', 'contact_list',
        'faq_list', 'job_list')
    PAGE_CHOICES = (
        (MAIN, _('main page')), (SCHEDULE, _('schedule page')), (SERVICES, _('services page')),
        (NEWS_LIST, _('news list page')), (NEWS_DETAIL, _('news detail page')), (DOCUMENTS, _('documents page')),
        (CONTACTS, _('contacts page')), (FAQ, _('faq page')), (JOB, _('job page')))

    page = models.CharField(verbose_name=_('page'), choices=PAGE_CHOICES, default=MAIN, max_length=50, unique=True)
    additional_header = models.TextField(verbose_name=_('additional header'), blank=True)
    additional_footer = models.TextField(verbose_name=_('additional footer'), blank=True)
    slider_proxy = models.TextField(verbose_name=_('slider proxy'), blank=True)
    enabled = models.BooleanField(verbose_name=_('enabled'), default=True, help_text=_('show/hide record.'))

    class Meta:
        ordering = ['page']
        verbose_name_plural = _('pages content')
        verbose_name = _('page content')
