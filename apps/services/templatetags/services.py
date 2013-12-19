from __future__ import absolute_import
from django import template
from services.models import ServiceType


register = template.Library()


@register.inclusion_tag('services/services_menu.html')
def services_menu():
    service_types = ServiceType.objects.published()
    return {
        'service_types': service_types,
    }
