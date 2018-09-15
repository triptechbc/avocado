# coding: utf-8
from conf.apps import *
from conf.etc import *

DEBUG = APP_SETTINGS.get('DEBUG')
PRODUCTION = APP_SETTINGS.get('PRODUCTION')

DATABASE_SETTINGS = APP_SETTINGS.get('DATABASE', {})

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_SETTINGS.get('NAME'),
        'USER': DATABASE_SETTINGS.get('USER'),
        'PASSWORD': DATABASE_SETTINGS.get('PASSWORD'),
        'HOST': DATABASE_SETTINGS.get('HOST', '127.0.0.1'),
        'PORT': DATABASE_SETTINGS.get('PORT', 5432),
    }
}

SITE_ID = 1

ADMINS = (
    ('Dmitry Astrikov', 'astrikov.d@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = APP_SETTINGS.get('ALLOWED_HOSTS', ['*'])

TIME_ZONE = 'PST8PDT'

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/data/'
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'www/data')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'www/static')

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = APP_SETTINGS.get('SECRET_KEY')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

INSTALLED_APPS = (
                     'django.contrib.auth',
                     'django.contrib.admin',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.sites',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.humanize',
                     'django.contrib.postgres',
                 ) + THIRD_PARTY_APPS + PROJECT_APPS

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

DATE_INPUT_FORMATS = (
    '%d.%m.Y'
)

DATETIME_INPUT_FORMATS = (
    '%d.%m.Y %H:%M:%S'
)

ROOT_URLCONF = 'app.urls'

AUTHENTICATION_BACKENDS = PROJECT_AUTHENTICATION_BACKENDS
