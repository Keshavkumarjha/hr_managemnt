# hr managemnt

its not use for real world its assesment projeect its not tested  if before use production

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy hr_managemnt

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd hr_managemnt
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd hr_managemnt
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd hr_managemnt
celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).


## Database configuration (env-based)

This project supports environment-driven database selection:

- **Local development (default): SQLite**
- **Production: PostgreSQL**

### Local (SQLite)

```bash
export DJANGO_SETTINGS_MODULE=config.settings.local
export DJANGO_DATABASE_ENGINE=sqlite
# optional: export SQLITE_PATH=/absolute/path/to/local.sqlite3
python manage.py migrate
python manage.py runserver
```

### Local (optional PostgreSQL)

```bash
export DJANGO_SETTINGS_MODULE=config.settings.local
export DJANGO_DATABASE_ENGINE=postgres
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_DB=hr_managemnt
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
python manage.py migrate
```

### Production (PostgreSQL)

Use `config.settings.production` with either:

- `DATABASE_URL=postgres://user:pass@host:5432/dbname`, or
- `POSTGRES_HOST/PORT/DB/USER/PASSWORD` vars (used to build a default URL).


## Railway deployment

1. Create a new Railway project and add a PostgreSQL plugin.
2. Set environment variables:
   - `DJANGO_SETTINGS_MODULE=config.settings.production`
   - `DJANGO_SECRET_KEY=<strong-secret>`
   - `DJANGO_ALLOWED_HOSTS=<your-railway-domain>`
   - `DJANGO_DATABASE_ENGINE=postgres`
   - `DATABASE_URL=<from Railway Postgres>`
   - `REDIS_URL=<optional>`
3. Railway will use `Procfile` and `railway.json` for start commands.
4. Verify static assets via WhiteNoise (collectstatic runs in Procfile).

See `RUN_LOCAL.md` for complete local setup.


## API documentation pages
- API home: `/api/`
- Swagger: `/api/docs/`
- ReDoc: `/api/redoc/`
- Reference index: `/api/reference/`
- OpenAPI schema JSON: `/api/schema/`

- Health check: `/healthz/`


### Railway free tier checklist

1. Add PostgreSQL plugin in Railway project.
2. Set minimum required env vars:
   - `DJANGO_SETTINGS_MODULE=config.settings.production`
   - `DJANGO_SECRET_KEY=<strong-secret>`
   - `DJANGO_ALLOWED_HOSTS=<your-domain>.up.railway.app`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-domain>.up.railway.app`
   - `DJANGO_DATABASE_ENGINE=postgres`
   - `DATABASE_URL=<Railway PostgreSQL URL>`
   - `RAILWAY_PUBLIC_DOMAIN=<your-domain>.up.railway.app`
3. Keep optional services disabled for free tier unless configured:
   - `DJANGO_USE_REDIS_CACHE=False`
   - `DJANGO_USE_S3_STORAGE=False`
4. Deploy. Railway runs `release` for migrations + collectstatic and starts Gunicorn web process.
5. Verify:
   - Home: `/`
   - Health: `/healthz/`
   - API home: `/api/`
   - Swagger docs: `/api/docs/`

### Manual steps required after first deploy
- Create admin user from Railway shell:
  - `python manage.py createsuperuser`
- If you later enable S3 media storage, set all `DJANGO_AWS_*` vars before redeploy.


### If build fails on Railway at pip install step
- This repo uses `psycopg[binary]` to avoid native compilation issues on free-tier builders.
- If you had previous failed builds, trigger a fresh deploy after clearing build cache in Railway.
- Keep `DJANGO_USE_S3_STORAGE=False` unless S3 variables are configured.
