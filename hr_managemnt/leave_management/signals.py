from django.db.models.signals import post_save
from django.dispatch import receiver

from hr_managemnt.audit.models import ActivityLog

from .models import LeaveRequest


@receiver(post_save, sender=LeaveRequest)
def log_leave_creation(sender, instance: LeaveRequest, created: bool, **kwargs):
    if created:
        ActivityLog.objects.create(
            actor=instance.employee.user,
            action="leave_requested",
            metadata={"leave_id": instance.id},
        )
