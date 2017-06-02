from django.contrib import admin

from core.models import PageContent


class PageContentAdmin(admin.ModelAdmin):

    list_display = ('page', 'enabled')


admin.site.register(PageContent, PageContentAdmin)
