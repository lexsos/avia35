from django.contrib import admin
from tinymce.widgets import AdminTinyMCE


class AdminTinymceMixin(object):

    rich_fields = []

    def get_rich_fields(self):
        return self.rich_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.get_rich_fields():
            kwargs['widget'] = AdminTinyMCE()
        return super(AdminTinymceMixin, self).formfield_for_dbfield(db_field, **kwargs)


class EnabledMixin(object):

    def make_enabled(self, request, queryset):
        queryset.update(enabled=True)

    def make_disabled(self, request, queryset):
        queryset.update(enabled=False)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'make_enabled' not in actions:
            action = (EnabledMixin.make_enabled, 'make_enabled', 'Включить выбранные %(verbose_name_plural)s')
            actions['make_enabled'] = action
        if 'make_disabled' not in actions:
            action = (EnabledMixin.make_disabled, 'make_disabled', 'Отключить выбранные %(verbose_name_plural)s')
            actions['make_disabled'] = action
        return actions


class WeightMixin(object):

    def zero_weight(self, request, queryset):
        queryset.update(weight=0)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'zero_weight' not in actions:
            action = (WeightMixin.zero_weight, 'zero_weight', 'Установить вес в 0 у выбранных %(verbose_name_plural)s')
            actions['zero_weight'] = action
        return actions


class PublicationAdmin(EnabledMixin, WeightMixin, admin.ModelAdmin):

    PUBLICATION_FIELDS = 'enabled', 'pub_date_start', 'pub_date_end', 'weight'

    list_filter = ('enabled', 'pub_date_start', 'weight')
    list_display = ('enabled', 'pub_date_start', 'pub_date_end', 'weight')
    list_per_page = 100
    date_hierarchy = 'pub_date_start'

    fieldsets = (('Параметры публикации', {'classes': ('wide',), 'fields': PUBLICATION_FIELDS}),)
