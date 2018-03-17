from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from main_page.models import Content


class ContentAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры содержимого', {'classes': ('wide',), 'fields': (
        'title', 'content_rich', 'content_plane')}), )

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    rich_fields = ('content_rich',)
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


admin.site.register(Content, ContentAdmin)
