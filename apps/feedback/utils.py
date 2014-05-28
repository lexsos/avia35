# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.models import Site

from .settings import CONFIG


def send_question_notice(question):
    address_to = CONFIG['NOTICE_TO']
    if address_to is None:
        return
    current_site = Site.objects.get_current()
    message = render_to_string(
        'feedback/question_mail.html',
        {
            'question': question,
            'domain': current_site.domain,
        }
    )
    theme = render_to_string(
        'feedback/question_mail_theme.html',
        {'question': question}
    )
    theme = theme.replace('\n', ' ')
    send_mail(theme, message, '', address_to, fail_silently=False)
