from rest_framework import serializers

from hr_managemnt.organization.models import Department
from hr_managemnt.organization.models import JobRole


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "code", "created_at", "updated_at"]


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = ["id", "title", "department", "description", "created_at", "updated_at"]
