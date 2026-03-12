# HRMS API Documentation

## Versioning
All domain endpoints are namespaced under `/api/v1/`.

## Authentication
- `POST /api/auth/jwt/` obtain access and refresh tokens.
- `POST /api/auth/jwt/refresh/` refresh access token.
- Use `Authorization: Bearer <access_token>`.

## OpenAPI
- Schema: `/api/schema/`
- Swagger UI: `/api/docs/`

## Core Endpoints
- Departments: `/api/v1/departments/`
- Roles: `/api/v1/roles/`
- Employees: `/api/v1/employees/`
- Employee Documents: `/api/v1/employee-documents/`
- Attendance: `/api/v1/attendance/`
- Leaves: `/api/v1/leaves/` (includes `/approve/` action)
- Payslips: `/api/v1/payslips/`
- Recruitment: `/api/v1/job-openings/`, `/api/v1/candidates/`, `/api/v1/applications/`
- Performance Reviews: `/api/v1/reviews/`
- Audit Logs: `/api/v1/activity-logs/`, `/api/v1/notifications/`

## Cross-cutting Standards
- Pagination: page number pagination (`page`, `page_size`).
- Filtering: `django-filter` on selected fields.
- Search + ordering for key list endpoints.
- Rate limiting: user and anonymous throttles.
- Permissions: read for authenticated users, write for HR Admin role/staff.


## Environment-based database strategy
- Local defaults to SQLite via `DJANGO_DATABASE_ENGINE=sqlite`.
- Production enforces PostgreSQL via `config.settings.production`.
- DB connection can be provided with `DATABASE_URL` or `POSTGRES_*` variables.
