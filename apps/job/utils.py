# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.models import Site

from .settings import CONFIG


def send_response_notice(response):
    address_to = CONFIG['NOTICE_TO']
    if address_to is None:
        return
    current_site = Site.objects.get_current()
    message = render_to_string(
        'job/response_mail.html',
        {
            'response': response,
            'domain': current_site.domain,
        }
    )
    theme = render_to_string(
        'job/response_mail_theme.html',
        {'response': response}
    )
    theme = theme.replace('\n', ' ')
    try:
        send_mail(theme, message, '', address_to, fail_silently=False)
    except:
        pass
