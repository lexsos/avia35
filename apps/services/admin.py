from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.admin import PublicationAdmin

from .models import ServiceType, Service, ServiceParametr, ServiceImage


class ServiceTypeAdmin(PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'slug', 'weight', 'enabled')

    fieldsets = (
        (
            _('Service type parameters'),
            {
                'classes': ('wide',),
                'fields': ('title', 'slug'),
            }
        ),
    ) + PublicationAdmin.fieldsets


class ServiceParametrInline(admin.StackedInline):
    model = ServiceParametr
    extra = 3


class ServiceImageInline(admin.StackedInline):
    model = ServiceImage
    extra = 3


class ServiceAdmin(PublicationAdmin):
    list_filter = ('service_type', 'weight', 'enabled')
    list_display = ('title', 'service_type', 'weight', 'enabled')

    fieldsets = (
        (
            _('Service parameters'),
            {
                'classes': ('wide',),
                'fields': ('service_type', 'title', 'description')
            }
        ),
    ) + PublicationAdmin.fieldsets

    inlines = [ServiceParametrInline, ServiceImageInline]


class ServiceParametrAdmin(admin.ModelAdmin):
    list_display = ('title', 'service')


class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'service')


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceParametr, ServiceParametrAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
