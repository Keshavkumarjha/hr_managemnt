from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("employees", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="PerformanceReview",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("review_period", models.CharField(max_length=32)),
                ("rating", models.PositiveSmallIntegerField()),
                ("comments", models.TextField(blank=True)),
                (
                    "employee",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="reviews", to="employees.employee"),
                ),
                (
                    "reviewer",
                    models.ForeignKey(on_delete=models.deletion.PROTECT, related_name="submitted_reviews", to="employees.employee"),
                ),
            ],
            options={"unique_together": {("employee", "review_period")}},
        ),
    ]
