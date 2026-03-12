from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel
from hr_managemnt.employees.models import Employee


class PerformanceReview(TimeStampedSoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="submitted_reviews")
    review_period = models.CharField(max_length=32)
    rating = models.PositiveSmallIntegerField()
    comments = models.TextField(blank=True)

    class Meta:
        unique_together = ("employee", "review_period")
