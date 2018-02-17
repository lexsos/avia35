from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from contacts.models import Contact


class ContactAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('Contact parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'content')
            }
        ),
    ) + PublicationAdmin.fieldsets

    #rich_fields = ('content',)


admin.site.register(Contact, ContactAdmin)
