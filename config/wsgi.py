from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.pro')

application = get_wsgi_application()

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.pro':
    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

    application = Sentry(application)
