from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin


from .models import Document, DocumentType, DocumentCategory


class DocumentAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled', 'doc_type')
    list_display = ('title', 'doc_type', 'weight', 'enabled')

    fieldsets = (
        (
            _('Document parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'doc_type', 'document',)
            }
        ),
    ) + PublicationAdmin.fieldsets


class DocumentCategoryAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    rich_fields = ('description',)

    fieldsets = (
        (
            _('document category parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'description',)
            }
        ),
    ) + PublicationAdmin.fieldsets


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
