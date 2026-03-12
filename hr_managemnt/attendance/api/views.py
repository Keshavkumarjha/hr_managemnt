from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from hr_managemnt.attendance.models import Attendance
from hr_managemnt.core.permissions import IsHRAdminOrReadOnly

from .serializers import AttendanceSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.active().select_related("employee")
    serializer_class = AttendanceSerializer
    permission_classes = [IsHRAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["employee", "work_date", "is_remote"]
