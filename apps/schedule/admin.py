from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import Flight, Agent


class FlightAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('direction', 'weight', 'enabled')

    fieldsets = (
        (_('Flight parameters'), {
            'classes': (
                'wide',
            ),
            'fields': (
                'direction',
                'departure',
                'arrival',
                'order',
                'agents',
            ),
        }),
    ) + PublicationAdmin.fieldsets

    rich_fields = ('departure', 'arrival', 'order')


class AgentAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Flight, FlightAdmin)
admin.site.register(Agent, AgentAdmin)
