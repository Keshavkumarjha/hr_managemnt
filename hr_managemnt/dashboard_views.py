from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render

from hr_managemnt.attendance.models import Attendance
from hr_managemnt.employees.models import Employee
from hr_managemnt.leave_management.models import LeaveRequest
from hr_managemnt.payroll.models import Payslip


@login_required
def dashboard(request):
    employees_count = Employee.objects.active().count()
    today_attendance = Attendance.objects.active().count()
    pending_leaves = LeaveRequest.objects.active().filter(status=LeaveRequest.Status.PENDING).count()
    payroll_avg = Payslip.objects.active().aggregate(avg=Avg("basic_pay"))["avg"] or 0

    context = {
        "employees_count": employees_count,
        "today_attendance": today_attendance,
        "pending_leaves": pending_leaves,
        "payroll_avg": payroll_avg,
    }
    return render(request, "pages/dashboard.html", context)


@login_required
def module_page(request, page_title: str):
    return render(request, "pages/module_page.html", {"page_title": page_title})


@login_required
def employees_page(request):
    return module_page(request, "Employee Management")


@login_required
def departments_page(request):
    return module_page(request, "Department Management")


@login_required
def attendance_page(request):
    return module_page(request, "Attendance Management")


@login_required
def leave_page(request):
    return module_page(request, "Leave Management")


@login_required
def payroll_page(request):
    return module_page(request, "Payroll")


@login_required
def profile_page(request):
    return module_page(request, "My Profile")
