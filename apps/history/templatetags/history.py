from __future__ import absolute_import

from django.template import Library


register = Library()


@register.inclusion_tag('history/side.html')
def history_side(side_content):

    return {
        'side_content': side_content,
    }
