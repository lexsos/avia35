from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from schedule.models import Flight, Agent, Note, PaymentBanner


class FlightAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (
        ('Параметры рейса', {'classes': ('wide'), 'fields': (
            'direction', 'flight_no', 'departure', 'arrival', 'order', 'agents')}),)

    list_filter = ('weight', 'enabled')
    list_display = ('direction', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets
    rich_fields = ('departure', 'arrival', 'order')


class AgentAdmin(admin.ModelAdmin):

    list_display = ('title', 'url')


class NoteAdmin(AdminTinymceMixin, PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры заметки', {'classes': ('wide',), 'fields': ('content',),}),)

    list_display = ('content', 'weight', 'enabled')
    rich_fields = ('content', )
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


class PaymentBannerAdmin(PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры банера', {'classes': ('wide',), 'fields': ('title', 'image')}),)

    list_display = ('title', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


admin.site.register(Flight, FlightAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(PaymentBanner, PaymentBannerAdmin)
