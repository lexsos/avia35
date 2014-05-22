from __future__ import absolute_import

from django.template import Library


register = Library()


@register.inclusion_tag('documents/document_table.html')
def document_table(caterogy):
    return {
        'document_list': caterogy.document_set.published(),
    }


