from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin

from .models import Vacancy, VacancyResponse


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


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(VacancyResponse, VacancyResponseAdmin)
