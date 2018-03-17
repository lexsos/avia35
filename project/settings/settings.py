import os

DEBUG = True

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..')
BASE_DIR = os.path.normpath(os.path.abspath(BASE_DIR))
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')
PROJECT_ROOT = os.path.normpath(os.path.abspath(PROJECT_ROOT))


ADMINS = (
    ('alexander', 'alexander@avia35.ru'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'var', 'public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'public', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'client'), )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'core.context_processors.additional_page_content',
            ],
        },
    },
]

PROJECT_APPS = (
    'slider',
    'job',
    'contacts',
    'documents',
    'avia_park',
    'news',
    'core',
    'schedule',
    'services',
    'main_page',
    'faq',
    'feedback',
    'robots',
    'history',
    'helpers',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'easy_thumbnails',
    'static_precompiler',
    'tinymce',
) + PROJECT_APPS

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

TINYMCE_SPELLCHECKER = True

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "spellchecker",
    'theme_advanced_buttons3_add': "|,spellchecker",
}

THUMBNAIL_ALIASES = {
    '': {
        'slider': {'size': (940, 320), 'crop': True},
        'craft_list': {'size': (290, 193), 'crop': True},
        'craft_detail': {'size': (440, 300), 'crop': True},
        'craft_detail_galery': {'size': (130, 88), 'crop': True},
        'news_list': {'size': (300, 200), 'crop': True},
        'news_detail': {'size': (450, 300), 'crop': True},
        'agent_logo': {'size': (130, 50), 'crop': True},
        'service': {'size': (220, 140), 'crop': True},
        'payment_banner': {'size': (120, 70), 'crop': True},
        'history_side_image': {'size': (140, 0), 'crop': True},
        'history_detail_hg': {'size': (0, 400), 'crop': True},
        'history_detail_wd': {'size': (500, 0), 'crop': True},
    },
}
THUMBNAIL_BASEDIR = 'thumbs'

EMAIL_HOST = 'smtp.avia35.ru'
EMAIL_PORT = '25'

JOB_CONFIG = {
    'NOTICE_TO': ('oup@avia35.ru', )
}

FEEDBACK_CONFIG = {
    'NOTICE_TO': ('avia_support@avia35.ru', )
}

SOUTH_MIGRATION_MODULES = {
    'captcha': 'captcha.south_migrations',
}

CAPTCHA_FILTER_FUNCTIONS = ('captcha.helpers.post_smooth',)
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_LENGTH = 4

FILE_UPLOAD_PERMISSIONS = 0o644

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'var', 'sqlite3.db'),
    }
}

ALLOWED_HOSTS = []

try:
    from .settings_local import *  # noqa
except ImportError:
    pass


if DEBUG:

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
