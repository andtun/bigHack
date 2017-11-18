from .base import *

# GENERAL

DEBUG = env.bool('DJANGO_DEBUG', True)
ADMIN_URL = '^admin/'
SECRET_KEY = 'super-secret-key'
ALLOWED_HOSTS = ['*']

# CELERY

INSTALLED_APPS += ['djcelery', 'kombu.transport.django']
BROKER_URL = 'django://'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# DEBUG TOOLBAR

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# CACHING

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
