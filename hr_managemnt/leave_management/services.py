from hr_managemnt.audit.models import ActivityLog
from hr_managemnt.audit.models import Notification
from hr_managemnt.leave_management.models import LeaveRequest


class LeaveApprovalService:
    @staticmethod
    def approve(leave: LeaveRequest, approver_employee) -> LeaveRequest:
        leave.status = LeaveRequest.Status.APPROVED
        leave.approved_by = approver_employee
        leave.save(update_fields=["status", "approved_by", "updated_at"])
        Notification.objects.create(
            recipient=leave.employee.user,
            title="Leave approved",
            body=f"Your leave request from {leave.start_date} to {leave.end_date} was approved.",
        )
        ActivityLog.objects.create(
            actor=approver_employee.user,
            action="leave_approved",
            metadata={"leave_id": leave.id, "employee_id": leave.employee_id},
        )
        return leave
