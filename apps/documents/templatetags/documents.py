from __future__ import absolute_import

from django.template import Library
from django.db.models import Count


register = Library()


@register.inclusion_tag('documents/document_table.html')
def document_table(caterogy, show_counters):
    document_list = caterogy.document_set.published()
    document_list = document_list.annotate(download_counter=Count('documentcounter'))
    return {'document_list': document_list, 'show_counters': show_counters}
