from rest_framework import serializers

from hr_managemnt.attendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["id", "employee", "work_date", "check_in", "check_out", "is_remote"]
