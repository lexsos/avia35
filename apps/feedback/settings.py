from django.conf import settings


CONFIG = {
    'NOTICE_TO': None,
}

CONFIG.update(getattr(settings, 'FEEDBACK_CONFIG', {}))
