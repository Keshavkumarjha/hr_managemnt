# Improved HRMS Architecture

## Domain Apps
- `organization`: departments and job roles.
- `employees`: employee lifecycle and document storage.
- `attendance`: attendance capture.
- `leave_management`: leave workflows and approvals.
- `payroll`: payslip domain.
- `recruitment`: hiring pipeline.
- `performance`: review cycles.
- `audit`: activity logs and notifications.
- `core`: shared base models and permission primitives.

## Patterns
- Service layer: `leave_management.services.LeaveApprovalService`
- Signals: leave creation activity logging.
- Soft delete base model for migration-safe retention.
- Versioned APIs under `/api/v1/*` using DRF routers.
