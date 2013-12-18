from django.contrib import admin
from dj_mixin.admin import AdminTinymceMixin
from dj_mixin.publications.admin import EnabledMixin

from .models import Slide


class SlideAdmin(AdminTinymceMixin, EnabledMixin, admin.ModelAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')
    rich_fields = ('title',)


admin.site.register(Slide, SlideAdmin)
