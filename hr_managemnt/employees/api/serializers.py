from rest_framework import serializers

from hr_managemnt.employees.models import Employee
from hr_managemnt.employees.models import EmployeeDocument


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "user",
            "employee_id",
            "department",
            "role",
            "date_of_joining",
            "status",
        ]


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        fields = ["id", "employee", "title", "file", "is_confidential", "created_at"]
