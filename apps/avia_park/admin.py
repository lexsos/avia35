from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin

from .models import Craft, CraftImage


class CraftAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'slug', 'weight', 'enabled')

    fieldsets = (
        (
            _('Craft parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'description', 'image', 'slug')
            }
        ),
    ) + PublicationAdmin.fieldsets


class CraftImageAdmin(admin.ModelAdmin):
    list_filter = ('craft',)
    list_display = ('craft', 'image')


admin.site.register(Craft, CraftAdmin)
admin.site.register(CraftImage, CraftImageAdmin)
