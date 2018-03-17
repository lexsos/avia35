from django.db import models
from helpers.models import Publication


class ServiceType(Publication):

    title = models.CharField(verbose_name='название', max_length=255)
    slug = models.CharField(verbose_name='slug', max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'типы услуг'
        verbose_name = 'тип услуги'
        ordering = ['-weight', 'title']

    def __str__(self):
        return self.title


class Service(Publication):

    service_type = models.ForeignKey(ServiceType, verbose_name='тип услуги', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)

    class Meta:
        verbose_name_plural = 'услуги'
        verbose_name = 'услуга'
        ordering = ['-weight', 'title']

    def __str__(self):
        return '{}:{}'.format(self.service_type.title, self.title)


class ServiceParametr(models.Model):

    service = models.ForeignKey(Service, verbose_name='услуга', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='заголовок', max_length=255)
    content = models.TextField(verbose_name='содержимое')

    class Meta:
        verbose_name_plural ='параметры услуги'
        verbose_name = 'параметр услуги'
        ordering = ['service', 'title']

    def __str__(self):
        return '{}:{}'.format(self.service.title, self.title)


class ServiceImage(models.Model):

    service = models.ForeignKey(Service, verbose_name='услуга', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='название', max_length=255)
    image = models.ImageField(verbose_name='изображение', upload_to='services')

    class Meta:
        verbose_name_plural = 'изображения услуг'
        verbose_name = 'изображение услуги'
        ordering = ['service', 'title']

    def __str__(self):
        return '{}:{}'.format(self.service.title, self.title)
