release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn config.wsgi --bind 0.0.0.0:${PORT:-8000} --log-file - --workers ${WEB_CONCURRENCY:-1} --threads ${GUNICORN_THREADS:-2} --timeout 120
