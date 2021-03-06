from django.contrib import admin

from helpers.admin import PublicationAdmin, AdminTinymceMixin
from services.models import ServiceType, Service, ServiceParametr, ServiceImage


class ServiceTypeAdmin(PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры типа услуги', {'classes': ('wide',), 'fields': ('title', 'slug')}),)

    list_filter = ('weight', 'enabled')
    list_display = ('title', 'slug', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets


class ServiceParametrInline(AdminTinymceMixin, admin.StackedInline):

    model = ServiceParametr
    rich_fields = ('content',)
    extra = 3


class ServiceImageInline(admin.StackedInline):

    model = ServiceImage
    extra = 3


class ServiceAdmin(PublicationAdmin):

    CUSTOM_FIELDS = (('Параметры услуги', {'classes': ('wide',), 'fields': ('service_type', 'title', 'description')}),)

    list_filter = ('service_type', 'weight', 'enabled')
    list_display = ('title', 'service_type', 'weight', 'enabled')
    fieldsets = CUSTOM_FIELDS + PublicationAdmin.fieldsets
    inlines = [ServiceParametrInline, ServiceImageInline]


class ServiceParametrAdmin(AdminTinymceMixin, admin.ModelAdmin):

    list_display = ('title', 'service')
    rich_fields = ('content',)


class ServiceImageAdmin(admin.ModelAdmin):

    list_display = ('title', 'service')


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceParametr, ServiceParametrAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
