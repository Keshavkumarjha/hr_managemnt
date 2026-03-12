from django.conf import settings
from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel
from hr_managemnt.organization.models import Department
from hr_managemnt.organization.models import JobRole


class Employee(TimeStampedSoftDeleteModel):
    class EmploymentStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        ON_LEAVE = "on_leave", "On Leave"
        EXITED = "exited", "Exited"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee_profile")
    employee_id = models.CharField(max_length=32, unique=True, db_index=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")
    role = models.ForeignKey(JobRole, on_delete=models.PROTECT, related_name="employees")
    date_of_joining = models.DateField()
    status = models.CharField(max_length=20, choices=EmploymentStatus.choices, default=EmploymentStatus.ACTIVE)


class EmployeeDocument(TimeStampedSoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="documents")
    title = models.CharField(max_length=160)
    file = models.FileField(upload_to="employee-documents/")
    is_confidential = models.BooleanField(default=True)
