from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from documents.models import Document, DocumentType, DocumentCategory, DocumentCounter


class DocumentAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled', 'doc_type', 'category')
    list_display = ('title', 'doc_type', 'weight', 'enabled', 'category')

    fieldsets = (
        (
            _('Document parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'doc_type', 'document', 'category')
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


class DocumentCounterAdmin(admin.ModelAdmin):
    list_display = ('access_date', 'client_ip', 'document')


admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)
admin.site.register(DocumentCounter, DocumentCounterAdmin)
