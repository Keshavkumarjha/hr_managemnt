from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel
from hr_managemnt.organization.models import Department


class JobOpening(TimeStampedSoftDeleteModel):
    title = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="openings")
    location = models.CharField(max_length=120)
    is_open = models.BooleanField(default=True, db_index=True)


class Candidate(TimeStampedSoftDeleteModel):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=25)


class Application(TimeStampedSoftDeleteModel):
    class Stage(models.TextChoices):
        APPLIED = "applied", "Applied"
        INTERVIEW = "interview", "Interview"
        OFFERED = "offered", "Offered"
        HIRED = "hired", "Hired"
        REJECTED = "rejected", "Rejected"

    opening = models.ForeignKey(JobOpening, on_delete=models.CASCADE, related_name="applications")
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="applications")
    stage = models.CharField(max_length=16, choices=Stage.choices, default=Stage.APPLIED, db_index=True)
