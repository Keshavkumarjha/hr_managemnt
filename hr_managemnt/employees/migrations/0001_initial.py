from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organization", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("employee_id", models.CharField(db_index=True, max_length=32, unique=True)),
                ("date_of_joining", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("on_leave", "On Leave"), ("exited", "Exited")],
                        default="active",
                        max_length=20,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(on_delete=models.deletion.PROTECT, related_name="employees", to="organization.department"),
                ),
                (
                    "role",
                    models.ForeignKey(on_delete=models.deletion.PROTECT, related_name="employees", to="organization.jobrole"),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=models.deletion.CASCADE, related_name="employee_profile", to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeDocument",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("title", models.CharField(max_length=160)),
                ("file", models.FileField(upload_to="employee-documents/")),
                ("is_confidential", models.BooleanField(default=True)),
                (
                    "employee",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="documents", to="employees.employee"),
                ),
            ],
        ),
    ]
