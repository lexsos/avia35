from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from helpers.admin import PublicationAdmin
from robots.models import RobotData


class RobotDataAdmin(PublicationAdmin):

    list_filter = ('weight', 'enabled')
    list_display = ('description', 'weight', 'enabled')

    fieldsets = (
        (
            _('Robot parameters'),
            {
                'classes': ('wide',),
                'fields': ('description', 'content', 'site')
            }
        ),
    ) + PublicationAdmin.fieldsets


admin.site.register(RobotData, RobotDataAdmin)
