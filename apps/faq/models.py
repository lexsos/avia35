from django.db import models
from helpers.models import Publication


class FrequentlyQuestion(Publication):

    title = models.CharField(verbose_name='заголовок', max_length=255)
    question = models.TextField(verbose_name='вопрос')
    answer = models.TextField(verbose_name='ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'часто задаваемые вопросы'
        verbose_name = 'часто задаваемый вопрос'
        ordering = ['-weight', '-pub_date_start']
