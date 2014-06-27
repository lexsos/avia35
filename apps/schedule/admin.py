from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin
from dj_mixin.admin import AdminTinymceMixin

from .models import Flight, Agent, Note, PaymentBanner


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
                'flight_no',
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


class PaymentBannerAdmin(PublicationAdmin):
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (_('Banner parameters'), {
            'classes': (
                'wide',
            ),
            'fields': (
                'title',
                'image',
            ),
        }),
    ) + PublicationAdmin.fieldsets


admin.site.register(Flight, FlightAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(PaymentBanner, PaymentBannerAdmin)
