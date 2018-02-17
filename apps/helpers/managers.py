from django.db import models
from helpers.querysets import PublicationQuerySet


class PublicationManager(models.Manager):

    """ Manager for access to public (is_show_site == True) objects """

    def __getattr__(self, attr, *args):
        """ Allow to use queryset methods from custom queryset
        more info: http://stackoverflow.com/a/2163921/4716629 """
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            # don't delegate internal methods to the queryset
            if attr.startswith('__') and attr.endswith('__'):
                raise
            return getattr(self.get_queryset(), attr, *args)

    def get_queryset(self):
        return getattr(self.model, 'QuerySet', PublicationQuerySet)(self.model, using=self._db)
