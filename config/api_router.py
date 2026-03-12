from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from hr_managemnt.attendance.api.views import AttendanceViewSet
from hr_managemnt.audit.api.views import ActivityLogViewSet
from hr_managemnt.audit.api.views import NotificationViewSet
from hr_managemnt.employees.api.views import EmployeeDocumentViewSet
from hr_managemnt.employees.api.views import EmployeeViewSet
from hr_managemnt.leave_management.api.views import LeaveRequestViewSet
from hr_managemnt.organization.api.views import DepartmentViewSet
from hr_managemnt.organization.api.views import JobRoleViewSet
from hr_managemnt.payroll.api.views import PayslipViewSet
from hr_managemnt.performance.api.views import PerformanceReviewViewSet
from hr_managemnt.recruitment.api.views import ApplicationViewSet
from hr_managemnt.recruitment.api.views import CandidateViewSet
from hr_managemnt.recruitment.api.views import JobOpeningViewSet
from hr_managemnt.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("v1/departments", DepartmentViewSet)
router.register("v1/roles", JobRoleViewSet)
router.register("v1/employees", EmployeeViewSet)
router.register("v1/employee-documents", EmployeeDocumentViewSet)
router.register("v1/attendance", AttendanceViewSet)
router.register("v1/leaves", LeaveRequestViewSet)
router.register("v1/payslips", PayslipViewSet)
router.register("v1/job-openings", JobOpeningViewSet)
router.register("v1/candidates", CandidateViewSet)
router.register("v1/applications", ApplicationViewSet)
router.register("v1/reviews", PerformanceReviewViewSet)
router.register("v1/activity-logs", ActivityLogViewSet)
router.register("v1/notifications", NotificationViewSet)

app_name = "api"
urlpatterns = router.urls
