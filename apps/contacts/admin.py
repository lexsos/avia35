from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from contacts.models import Contact


class ContactAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (
        ('Параметры контактов', {'classes': ('wide',), 'fields': ('title', 'content')}),)

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


admin.site.register(Contact, ContactAdmin)
