from django.contrib import admin

from helpers.admin import PublicationAdmin
from avia_park.models import Craft, CraftImage


class CraftAdmin(PublicationAdmin):

    CUSTOM_FIELDS = (
        ('Параметры судна', {'classes': ('wide',), 'fields': ('title', 'description', 'image', 'slug')}),)

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'slug', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


class CraftImageAdmin(admin.ModelAdmin):
    list_filter = ('craft',)
    list_display = ('craft', 'image')


admin.site.register(Craft, CraftAdmin)
admin.site.register(CraftImage, CraftImageAdmin)
