from decimal import Decimal

from django.db import models

from hr_managemnt.core.models import TimeStampedSoftDeleteModel
from hr_managemnt.employees.models import Employee


class Payslip(TimeStampedSoftDeleteModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="payslips")
    period_start = models.DateField()
    period_end = models.DateField()
    basic_pay = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    allowances = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    deductions = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    @property
    def net_pay(self):
        return self.basic_pay + self.allowances - self.deductions
