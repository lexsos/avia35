from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from news.models import News


class NewsAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры новости', {'classes': ('wide',), 'fields': (
        'title', 'preview', 'content', 'image',)}), )

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets
    rich_fields = ('preview', 'content')


admin.site.register(News, NewsAdmin)
