from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from news.models import News


class NewsAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('News parameters'),
            {
                'classes': ('wide',),
                'fields': (
                    'title',
                    'preview',
                    'content',
                    'image',
                )
            }
        ),
    ) + PublicationAdmin.fieldsets

    rich_fields = ('preview', 'content')


admin.site.register(News, NewsAdmin)
