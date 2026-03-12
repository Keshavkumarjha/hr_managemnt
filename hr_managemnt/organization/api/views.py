from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from hr_managemnt.core.permissions import IsHRAdminOrReadOnly
from hr_managemnt.organization.models import Department
from hr_managemnt.organization.models import JobRole

from .serializers import DepartmentSerializer
from .serializers import JobRoleSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.active()
    serializer_class = DepartmentSerializer
    permission_classes = [IsHRAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "code"]
    ordering_fields = ["name", "created_at"]


class JobRoleViewSet(ModelViewSet):
    queryset = JobRole.objects.active().select_related("department")
    serializer_class = JobRoleSerializer
    permission_classes = [IsHRAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "department__name"]
