from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import Vacancy, VacancyResponse, Note


class VacancyAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('Vacancy parameters'),
            {
                'classes': ('wide',),
                'fields': (
                    'title',
                    'description',
                    'requirements',
                    'schedule',
                    'payment',
                    'contacts',
                    'additionally',
                )
            }
        ),
    ) + PublicationAdmin.fieldsets


class VacancyResponseAdmin(admin.ModelAdmin):
    list_filter = ('vacancy',)
    list_display = ('vacancy', 'create_date', 'fio', 'phone')


class NoteAdmin(AdminTinymceMixin, PublicationAdmin):
    list_display = ('content', 'weight', 'enabled')
    rich_fields = ('content')

    fieldsets = (
        (_('Note parameters'), {
            'classes': (
                'wide',
            ),
            'fields': (
                'content',
            ),
        }),
    ) + PublicationAdmin.fieldsets


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(VacancyResponse, VacancyResponseAdmin)
admin.site.register(Note, NoteAdmin)
