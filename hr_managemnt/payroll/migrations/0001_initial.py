from decimal import Decimal

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("employees", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Payslip",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("period_start", models.DateField()),
                ("period_end", models.DateField()),
                ("basic_pay", models.DecimalField(decimal_places=2, default=Decimal("0.00"), max_digits=12)),
                ("allowances", models.DecimalField(decimal_places=2, default=Decimal("0.00"), max_digits=12)),
                ("deductions", models.DecimalField(decimal_places=2, default=Decimal("0.00"), max_digits=12)),
                (
                    "employee",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="payslips", to="employees.employee"),
                ),
            ],
        ),
    ]
