from django.db import models
from helpers.models import Publication


class Agent(models.Model):

    title = models.CharField(verbose_name='название', max_length=255)
    url = models.URLField(verbose_name='ссылка')
    image = models.ImageField(verbose_name='логотип', upload_to='schedule', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'агенты'
        verbose_name = 'агент'
        ordering = ['title']

    def __str__(self):
        return self.title


class Flight(Publication):

    direction = models.CharField(verbose_name='наравление рейса', max_length=255)
    flight_no = models.CharField(verbose_name='номер рейса', max_length=255, blank=True)
    departure = models.TextField(verbose_name='вылет')
    arrival = models.TextField(verbose_name='прибытие')
    order = models.TextField(verbose_name='заказ билета', blank=True)
    agents = models.ManyToManyField(Agent, verbose_name='агенты', blank=True)

    class Meta:
        verbose_name_plural = 'рейсы'
        verbose_name = 'рейс'
        ordering = ['-weight', 'direction']

    def __str__(self):
        return self.direction


class Note(Publication):

    content = models.TextField(verbose_name='содержание заметки')

    class Meta:
        verbose_name_plural = 'заметки'
        verbose_name = 'заметка'
        ordering = ['-weight', 'content']

    def __str__(self):
        return self.content


class PaymentBanner(Publication):

    image = models.ImageField(verbose_name='изображение', upload_to='schedule')
    title = models.CharField(verbose_name='название', max_length=255)

    class Meta:
        verbose_name_plural = 'банеры платежных систем'
        verbose_name = 'банер платежной системы'
        ordering = ['-weight', 'title']

    def __str__(self):
        return self.title
