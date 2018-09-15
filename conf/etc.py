# coding: utf-8
import json
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(PROJECT_ROOT, 'settings.json'), 'r') as settings_fd:
    APP_SETTINGS = json.loads(settings_fd.read())

# URL settings
APP_URL = APP_SETTINGS.get('APP_URL')
PORT = APP_SETTINGS.get('PORT', 80)

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

RAVEN_CONFIG = {
    'dsn': APP_SETTINGS.get('RAVEN_DSN', '')
}

PROJECT_AUTHENTICATION_BACKENDS = [
    'app.users.backends.UserAuthBackend',
]

AUTH_USER_MODEL = 'users.User'
