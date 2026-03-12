from rest_framework import serializers

from hr_managemnt.leave_management.models import LeaveRequest


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ["id", "employee", "start_date", "end_date", "reason", "status", "approved_by"]

    def validate(self, attrs):
        if attrs["end_date"] < attrs["start_date"]:
            raise serializers.ValidationError("end_date must be greater than or equal to start_date")
        return attrs
