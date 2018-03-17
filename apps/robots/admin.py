from django.contrib import admin

from helpers.admin import PublicationAdmin
from robots.models import RobotData


class RobotDataAdmin(PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры поискового робота', {'classes': ('wide',), 'fields': (
        'description', 'content', 'site')}), )

    list_filter = ('weight', 'enabled')
    list_display = ('description', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


admin.site.register(RobotData, RobotDataAdmin)
