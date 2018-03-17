from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from job.models import Vacancy, VacancyResponse, Note


class VacancyAdmin(PublicationAdmin):

    CUSTOM_FIELDS = (
        ('Параметры вакансии', {'classes': ('wide',), 'fields': (
            'title',  'description', 'requirements', 'schedule', 'payment', 'contacts', 'additionally')}), )

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


class VacancyResponseAdmin(admin.ModelAdmin):

    list_filter = ('vacancy', )
    list_display = ('vacancy', 'create_date', 'fio', 'phone')


class NoteAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры заметки', {'classes': ('wide'), 'fields': ('content',)}), )

    list_display = ('content', 'weight', 'enabled')
    rich_fields = ('content', )
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(VacancyResponse, VacancyResponseAdmin)
admin.site.register(Note, NoteAdmin)
