from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import ContentBlock, SideContent


class ContentBlockAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('name', 'weight', 'enabled')

    fieldsets = (
        (
            _('content block parameters'),
            {
                'classes': ('wide',),
                'fields': ('name', 'content_rich', 'content_plane')
            }
        ),
    ) + PublicationAdmin.fieldsets

    rich_fields = ('content_rich', )


class SideContentAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled', 'content_block')
    list_display = ('name', 'content_block', 'side', 'weight', 'enabled')

    fieldsets = (
        (
            _('side content parameters'),
            {
                'classes': ('wide',),
                'fields': (
                    'name',
                    'content_block',
                    'side',
                    'image',
                    'content_rich',
                    'content_plane',
                )
            }
        ),
        (
            _('detail img parameters'),
            {
                'classes': ('wide',),
                'fields': (
                    'detail_content_rich',
                    'detail_content_plane',
                    'detail_img_adjustment',
                )
            }
        ),
    ) + PublicationAdmin.fieldsets

    rich_fields = (
        'content_rich',
        'detail_content_rich',
    )


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(SideContent, SideContentAdmin)
