web: gunicorn config.wsgi --log-file -
worker: celery worker --app=config.celery.app
release: python manage.py migrate
