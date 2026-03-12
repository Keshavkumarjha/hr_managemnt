release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn config.wsgi --log-file - --workers 2 --timeout 120
