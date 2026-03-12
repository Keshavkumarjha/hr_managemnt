from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from hr_managemnt.core.permissions import IsHRAdminOrReadOnly
from hr_managemnt.employees.models import Employee
from hr_managemnt.leave_management.models import LeaveRequest
from hr_managemnt.leave_management.services import LeaveApprovalService

from .serializers import LeaveRequestSerializer


class LeaveRequestViewSet(ModelViewSet):
    queryset = LeaveRequest.objects.active().select_related("employee", "approved_by")
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsHRAdminOrReadOnly]

    @action(methods=["post"], detail=True)
    def approve(self, request, pk=None):
        leave = self.get_object()
        approver = Employee.objects.get(user=request.user)
        leave = LeaveApprovalService.approve(leave=leave, approver_employee=approver)
        serializer = self.get_serializer(leave)
        return Response(serializer.data)
