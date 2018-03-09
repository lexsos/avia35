from django.db import models
from helpers.models import Publication


class Craft(Publication):

    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(verbose_name='изображение судна', upload_to='avia_park')
    slug = models.CharField(verbose_name='slug', max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_images(self):
        return CraftImage.objects.filter(craft=self)

    def get_first_image(self):
        qs = self.get_images()
        if qs.exists():
            return qs[0].image
        return self.image

    class Meta:
        verbose_name_plural = 'суда'
        verbose_name = 'судно'
        ordering = ['-weight', '-pub_date_start']


class CraftImage(models.Model):

    craft = models.ForeignKey(Craft, on_delete=models.CASCADE, verbose_name='судно')
    image = models.ImageField(verbose_name='изображение судна', upload_to='avia_park')

    def __str__(self):
        return '{0}:{1}'.format(self.craft.title, self.image)

    class Meta:
        verbose_name_plural = 'изображения судов'
        verbose_name = 'изображение судна'
        ordering = ['craft__title']
