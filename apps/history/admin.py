from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from history.models import ContentBlock, SideContent


class ContentBlockAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (
        ('параметры блока', {'classes': ('wide',), 'fields': ('name', 'content_rich', 'content_plane')}),)

    list_filter = ('weight', 'enabled')
    list_display = ('name', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets
    rich_fields = ('content_rich', )


class SideContentAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS =(
        ('параметры содержимого стороны', {'classes': ('wide',), 'fields': (
            'name', 'content_block', 'side', 'image', 'content_rich', 'content_plane')}),
        ('параметры детального изображения', {'classes': ('wide',), 'fields': (
            'detail_content_rich', 'detail_content_plane', 'detail_img_adjustment')}))

    list_filter = ('weight', 'enabled', 'content_block')
    list_display = ('name', 'content_block', 'side', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets
    rich_fields = ('content_rich', 'detail_content_rich')


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(SideContent, SideContentAdmin)
