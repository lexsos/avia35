from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from faq.models import FrequentlyQuestion


class FrequentlyQuestionAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('frequently question parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'question', 'answer')
            }
        ),
    ) + PublicationAdmin.fieldsets

    rich_fields = ('question', 'answer')


admin.site.register(FrequentlyQuestion, FrequentlyQuestionAdmin)
