from django.conf import settings


CONFIG = {
    'SMALL_FAQ': 5,
}

CONFIG.update(getattr(settings, 'FAQ_CONFIG', {}))
