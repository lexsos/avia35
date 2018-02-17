from django.contrib import admin

from helpers.admin import AdminTinymceMixin, EnabledMixin
from slider.models import Slide


class SlideAdmin(AdminTinymceMixin, EnabledMixin, admin.ModelAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    rich_fields = ('title',)


admin.site.register(Slide, SlideAdmin)
