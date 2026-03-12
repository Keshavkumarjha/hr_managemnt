from django.conf import settings
from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel


class ActivityLog(TimeStampedSoftDeleteModel):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=120)
    metadata = models.JSONField(default=dict, blank=True)


class Notification(TimeStampedSoftDeleteModel):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=140)
    body = models.TextField()
    is_read = models.BooleanField(default=False, db_index=True)
