from rest_framework.viewsets import ReadOnlyModelViewSet

from hr_managemnt.audit.models import ActivityLog
from hr_managemnt.audit.models import Notification
from hr_managemnt.core.permissions import IsHRAdminOrReadOnly

from .serializers import ActivityLogSerializer
from .serializers import NotificationSerializer


class ActivityLogViewSet(ReadOnlyModelViewSet):
    queryset = ActivityLog.objects.active().select_related("actor")
    serializer_class = ActivityLogSerializer
    permission_classes = [IsHRAdminOrReadOnly]


class NotificationViewSet(ReadOnlyModelViewSet):
    queryset = Notification.objects.active().select_related("recipient")
    serializer_class = NotificationSerializer
    permission_classes = [IsHRAdminOrReadOnly]
