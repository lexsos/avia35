from django.db import models


class Slide(models.Model):

    title = models.TextField(verbose_name='заголовок слайда', help_text='текст который будет отображаться на слайде')
    image = models.ImageField(verbose_name='изображение слайда', upload_to='slider')
    weight = models.IntegerField(verbose_name='вес', default=0, help_text='определяет порядок отображения слайдов')
    enabled = models.BooleanField(
        verbose_name='включено', default=True, help_text='если установленo, слайд будет отображаться')

    class Meta:
        ordering = ['-weight']
        verbose_name_plural = 'слайды'
        verbose_name = 'слайд'

    def __str__(self):
        return self.title
