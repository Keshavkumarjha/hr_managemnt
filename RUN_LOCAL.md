# Run HRMS Locally

## 1) Create virtual environment
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements/local.txt
```

## 2) Configure environment
```bash
cp .env.example .env
export DJANGO_READ_DOT_ENV_FILE=True
```

Use SQLite (default local):
```bash
export DJANGO_SETTINGS_MODULE=config.settings.local
export DJANGO_DATABASE_ENGINE=sqlite
```

Optional PostgreSQL locally:
```bash
export DJANGO_DATABASE_ENGINE=postgres
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export POSTGRES_DB=hr_managemnt
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
```

## 3) Database + superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

## 4) Run server
```bash
python manage.py runserver
```

## 5) Useful URLs
- Landing page: `http://127.0.0.1:8000/`
- Dashboard: `http://127.0.0.1:8000/dashboard/`
- API docs: `http://127.0.0.1:8000/api/docs/`
- API reference: `http://127.0.0.1:8000/api/reference/`
- API health: `http://127.0.0.1:8000/api/v1/health/`
- Admin: `http://127.0.0.1:8000/admin/`

## 6) JWT auth (API)
```bash
curl -X POST http://127.0.0.1:8000/api/auth/jwt/ \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com", "password": "your-password"}'
```
