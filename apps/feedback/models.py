from django.db import models


class Question(models.Model):

    fio = models.CharField(verbose_name='ФИО', max_length=255)
    contact = models.CharField(verbose_name='контакты', max_length=255)
    content = models.TextField(verbose_name='вопрос')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    answered = models.BooleanField(default=False, verbose_name='отвечено')

    def __str__(self):
        return '{}:{}'.format(self.fio, self.contact)

    class Meta:
        verbose_name_plural = 'вопросы'
        verbose_name = 'вопрос'
        ordering = ['-create_date']
