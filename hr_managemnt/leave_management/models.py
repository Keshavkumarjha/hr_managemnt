from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel
from hr_managemnt.employees.models import Employee


class LeaveRequest(TimeStampedSoftDeleteModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="leave_requests")
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING, db_index=True)
    approved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="approved_leaves")

    class Meta:
        indexes = [models.Index(fields=["status", "start_date"])]
