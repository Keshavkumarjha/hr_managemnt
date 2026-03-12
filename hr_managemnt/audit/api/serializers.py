from rest_framework import serializers

from hr_managemnt.audit.models import ActivityLog
from hr_managemnt.audit.models import Notification


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ["id", "actor", "action", "metadata", "created_at"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["id", "recipient", "title", "body", "is_read", "created_at"]
