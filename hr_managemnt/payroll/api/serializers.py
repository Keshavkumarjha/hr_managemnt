from rest_framework import serializers

from hr_managemnt.payroll.models import Payslip


class PayslipSerializer(serializers.ModelSerializer):
    net_pay = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Payslip
        fields = [
            "id",
            "employee",
            "period_start",
            "period_end",
            "basic_pay",
            "allowances",
            "deductions",
            "net_pay",
        ]
