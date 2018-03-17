from django.db import models
from helpers.models import Publication


class News(Publication):

    title = models.CharField(verbose_name='заголовок', max_length=255)
    preview = models.TextField(verbose_name='анонс')
    content = models.TextField(verbose_name='содержимое', blank=True)
    image = models.ImageField(verbose_name='изображение', upload_to='news')

    class Meta:
        verbose_name_plural = 'новости'
        verbose_name = 'новость'
        ordering = ['-weight', '-pub_date_start']

    def get_content(self):
        if self.content:
            return self.content
        return self.preview

    def __str__(self):
        return self.title
