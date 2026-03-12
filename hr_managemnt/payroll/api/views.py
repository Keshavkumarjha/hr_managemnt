from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from hr_managemnt.core.permissions import IsHRAdminOrReadOnly
from hr_managemnt.payroll.models import Payslip

from .serializers import PayslipSerializer


class PayslipViewSet(ModelViewSet):
    queryset = Payslip.objects.active().select_related("employee")
    serializer_class = PayslipSerializer
    permission_classes = [IsHRAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["employee", "period_start", "period_end"]
