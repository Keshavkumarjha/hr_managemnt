from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from hr_managemnt.core.permissions import IsHRAdminOrReadOnly
from hr_managemnt.employees.models import Employee
from hr_managemnt.employees.models import EmployeeDocument

from .serializers import EmployeeDocumentSerializer
from .serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.active().select_related("user", "department", "role")
    serializer_class = EmployeeSerializer
    permission_classes = [IsHRAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["department", "role", "status"]
    search_fields = ["employee_id", "user__email", "user__name"]
    ordering_fields = ["created_at", "date_of_joining"]


class EmployeeDocumentViewSet(ModelViewSet):
    queryset = EmployeeDocument.objects.active().select_related("employee")
    serializer_class = EmployeeDocumentSerializer
    permission_classes = [IsHRAdminOrReadOnly]
