from __future__ import absolute_import
from django import template
from slider.models import Slide


register = template.Library()


@register.inclusion_tag('slider/slider.html')
def show_slider():
    slides = Slide.objects.filter(enabled=True)
    first_pk = None
    if slides.exists():
        first_pk = slides[0].pk
    return {'slides': slides, 'first_pk': first_pk}
