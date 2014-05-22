from __future__ import absolute_import
from django import template

from schedule.models import Note, PaymentBanner


register = template.Library()


@register.inclusion_tag('schedule/notes.html')
def show_notes():
    note_list = Note.objects.published()
    return {
        'note_list': note_list,
    }


@register.inclusion_tag('schedule/payment_banners.html')
def show_payment_banners():
    benner_list = PaymentBanner.objects.published()
    return {
        'benner_list': benner_list,
    }
