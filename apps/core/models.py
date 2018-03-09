from django.db import models


class PageContent(models.Model):

    MAIN, SCHEDULE, SERVICES, NEWS_LIST, NEWS_DETAIL, DOCUMENTS, CONTACTS, FAQ, JOB = (
        'main_page', 'schedule_list', 'services_list', 'news_list', 'news_detail', 'document_list', 'contact_list',
        'faq_list', 'job_list')
    PAGE_CHOICES = (
        (MAIN, 'главна'), (SCHEDULE, 'расписание'), (SERVICES, 'услуги'), (NEWS_LIST, 'список новостей'),
        (NEWS_DETAIL, 'страница новости'), (DOCUMENTS, 'документы'), (CONTACTS, 'контакты'), (FAQ, 'faq'),
        (JOB, 'вакансии'))

    page = models.CharField(verbose_name='страница', choices=PAGE_CHOICES, default=MAIN, max_length=50, unique=True)
    additional_header = models.TextField(verbose_name='дополнительный заголовк', blank=True)
    additional_footer = models.TextField(verbose_name='дополнительный подвал', blank=True)
    slider_proxy = models.TextField(verbose_name='слайдер', blank=True)
    enabled = models.BooleanField(verbose_name='включено', default=True)

    class Meta:
        ordering = ['page']
        verbose_name_plural = 'содержимое страниц'
        verbose_name = 'содержимое страницы'

    def __str__(self):
        return self.page

    @classmethod
    def get_content(cls, page):
        try:
            return cls.objects.get(enabled=True, page=page)
        except cls.DoesNotExist:
            pass
