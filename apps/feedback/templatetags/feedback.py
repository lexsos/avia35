from __future__ import absolute_import
from django import template
from django.conf import settings

from feedback.forms import QuestionForm

register = template.Library()


@register.inclusion_tag('feedback/tag/feedback_form.html')
def feedback_form():
    return {
        'form': QuestionForm(),
        'STATIC_URL': settings.STATIC_URL,
    }
