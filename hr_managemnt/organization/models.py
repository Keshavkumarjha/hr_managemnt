from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel


class Department(TimeStampedSoftDeleteModel):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=20, unique=True, db_index=True)

    def __str__(self):
        return self.name


class JobRole(TimeStampedSoftDeleteModel):
    title = models.CharField(max_length=140, db_index=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="roles")
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("title", "department")

    def __str__(self):
        return self.title
