from django.db import models
from helpers.models import Publication


class Vacancy(Publication):
    title = models.CharField(verbose_name='наименование', max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)
    requirements = models.TextField(verbose_name='требования', blank=True)
    schedule = models.CharField(verbose_name='график работы', max_length=255, blank=True)
    payment = models.CharField(verbose_name='оплата', max_length=255, blank=True)
    contacts = models.CharField(verbose_name='контакты работодателя', max_length=255, blank=True)
    additionally = models.TextField(verbose_name='дополнительная информация', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'вакансии'
        verbose_name = 'вакансия'
        ordering = ['-weight', '-pub_date_start']


class VacancyResponse(models.Model):

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='вакансия')
    fio = models.CharField(verbose_name='ФИО соискателя', max_length=255)
    phone = models.CharField(verbose_name='телефон соискателя', max_length=255)
    about_self = models.TextField(verbose_name='о себе', blank=True)
    summary = models.FileField(upload_to='job', verbose_name='резюме соискателя', blank=True)
    create_date = models.DateTimeField(auto_now=True, verbose_name='дата отклика')

    def __str__(self):
        return '{}:{}'.format(self.vacancy.title, self.fio)

    class Meta:
        verbose_name_plural = 'отклики на вакансии'
        verbose_name = 'отклик на вакансию'
        ordering = ['-create_date']


class Note(Publication):

    content = models.TextField(verbose_name='содержание заметки')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'заметки'
        verbose_name = 'заметка'
        ordering = ['-weight', 'content']
