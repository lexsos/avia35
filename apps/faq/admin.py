from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from faq.models import FrequentlyQuestion


class FrequentlyQuestionAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (
        ('часто задаваемые вопросы', {'classes': ('wide',), 'fields': ('title', 'question', 'answer')}),)

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets
    rich_fields = ('question', 'answer')


admin.site.register(FrequentlyQuestion, FrequentlyQuestionAdmin)
