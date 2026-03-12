from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel
from hr_managemnt.employees.models import Employee


class Attendance(TimeStampedSoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance_records")
    work_date = models.DateField(db_index=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    is_remote = models.BooleanField(default=False)

    class Meta:
        unique_together = ("employee", "work_date")
        indexes = [models.Index(fields=["employee", "work_date"])]
