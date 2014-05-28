from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import FrequentlyQuestion


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
