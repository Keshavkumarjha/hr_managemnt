from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("employees", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("work_date", models.DateField(db_index=True)),
                ("check_in", models.DateTimeField()),
                ("check_out", models.DateTimeField(blank=True, null=True)),
                ("is_remote", models.BooleanField(default=False)),
                (
                    "employee",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="attendance_records", to="employees.employee"),
                ),
            ],
            options={"unique_together": {("employee", "work_date")}},
        ),
        migrations.AddIndex(
            model_name="attendance",
            index=models.Index(fields=["employee", "work_date"], name="attendance_e_work_da_680fb6_idx"),
        ),
    ]
