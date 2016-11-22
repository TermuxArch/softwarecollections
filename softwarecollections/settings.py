"""
Django settings for softwarecollections project.

Generated by 'django-admin startproject' using Django 1.9.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# import ugettext_lazy to avoid circular module import
from django.utils.translation import ugettext_lazy as _

# localsettings is used to store site depandant settings
from .localsettings import (
    BASE_DIR, SECRET_KEY, DEBUG, DBDEBUG, ALLOWED_HOSTS, DATABASES,
    ADMINS, MANAGERS, SERVER_EMAIL,
    COPR_URL, COPR_API_URL, COPR_COPRS_URL,
    LANGUAGE_CODE, TIME_ZONE, LANGUAGES,
    MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL, REPOS_ROOT, REPOS_URL,
    YUM_CACHE_ROOT, RPMBUILD_TOPDIR
)


# Application definition

INSTALLED_APPS = [
    'softwarecollections',
    'softwarecollections.scls',
    'softwarecollections.auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown2',
    'tagging',
    'sekizai',
    'captcha',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'softwarecollections.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'softwarecollections.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        '': {
            'handlers': DEBUG and ['console'] or ['console', 'mail_admins'],
            'level':    DEBUG and 'DEBUG'     or 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': DBDEBUG and 'DEBUG' or 'INFO',
            'propagate': True,
        },
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

USE_I18N = True

USE_L10N = True

USE_TZ = True

##################
# AUTHENTICATION #
##################

AUTH_USER_MODEL = 'auth.User'

AUTHENTICATION_BACKENDS = (
    'softwarecollections.auth.backend.PerObjectModelBackend',
    'fas.backend.FasBackend',
)

LOGIN_URL = '/login/'

LOGOUT_URL = '/logout/'

LOGIN_REDIRECT_URL = '/'

# The number of days a password reset link is valid for
PASSWORD_RESET_TIMEOUT_DAYS = 3

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'softwarecollections',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

CAPTCHA_FONT_SIZE        = 32
CAPTCHA_LETTER_ROTATION  = None
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
CAPTCHA_FOREGROUND_COLOR = '#001100'
CAPTCHA_CHALLENGE_FUNCT  = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS  = ()
CAPTCHA_FILTER_FUNCTIONS = ()
CAPTCHA_FLITE_PATH       = '/usr/bin/flite'
CAPTCHA_TIMEOUT          = 20

