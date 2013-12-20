from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class Craft(Publication):
    title = models.CharField(
        verbose_name=_('craft title'),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_('craft description'),
        blank=True,
    )
    image = models.ImageField(
        verbose_name=_('craft image'),
        upload_to='avia_park',
    )
    slug = models.CharField(
        verbose_name=_('craft slug'),
        max_length=255,
        unique=True,
    )

    def __unicode__(self):
        return self.title

    def get_images(self):
        return CraftImage.objects.filter(craft=self)

    def get_first_image(self):
        qs = self.get_images()
        if qs.exists():
            return qs[0].image
        return self.image

    class Meta:
        verbose_name_plural = _('crafts')
        verbose_name = _('craft')
        ordering = ['-weight', '-pub_date_start']


class CraftImage(models.Model):

    craft = models.ForeignKey(
        Craft,
        verbose_name=_('craft'),
    )
    image = models.ImageField(
        verbose_name=_('craft image'),
        upload_to='avia_park',
    )

    def __unicode__(self):
        return u'{0}:{1}'.format(self.craft.title, self.image)

    class Meta:
        verbose_name_plural = _('crafts images')
        verbose_name = _('craft image')
        ordering = ['craft__title']
