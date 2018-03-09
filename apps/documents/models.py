import os

from django.db import models
from helpers.models import Publication


class DocumentType(models.Model):

    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'типы документов'
        verbose_name = 'тип документа'
        ordering = ['title']


class DocumentCategory(Publication):

    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'категории документов'
        verbose_name = 'категория документа'
        ordering = ['-weight', 'pub_date_start']


class Document(Publication):

    doc_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, verbose_name='тип документа')
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, verbose_name='категория документа')
    title = models.CharField(verbose_name='название', max_length=255)
    document = models.FileField(upload_to='documents', verbose_name='файл')

    def get_size_text(self):
        if (not self.document) or (not os.path.exists(self.document.path)):
            return '{0} {1}'.format(0, 'байт')
        size = self.document.size
        unit = 'байт'
        if size > 1024:
            size = size/1024.0
            unit = 'Кб'
        if size > 1024:
            size = size/1024.0
            unit = 'Мб'
        if size > 1024:
            size = size/1024.0
            unit = 'Гб'
        return '{0:0.1f} {1}'.format(size, unit)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'документы'
        verbose_name = 'документ'
        ordering = ['-weight', 'pub_date_start']


class DocumentCounter(models.Model):

    access_date = models.DateTimeField(auto_now=True, verbose_name='дата доступа')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='документ')
    client_ip = models.GenericIPAddressField(verbose_name='ip адрес пользователя', blank=True, null=True)
    user_agent = models.TextField(verbose_name='веб-браузер', blank=True)

    def __str__(self):
        return '{0}:{1}'.format(self.access_date, self.document.title)

    class Meta:
        verbose_name_plural = 'счетчики документов'
        verbose_name = 'счетчик документа'
        ordering = ['access_date']
