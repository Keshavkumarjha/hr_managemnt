from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("organization", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("full_name", models.CharField(max_length=120)),
                ("email", models.EmailField(db_index=True, max_length=254)),
                ("phone", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="JobOpening",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("title", models.CharField(max_length=120)),
                ("location", models.CharField(max_length=120)),
                ("is_open", models.BooleanField(db_index=True, default=True)),
                (
                    "department",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="openings", to="organization.department"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("applied", "Applied"),
                            ("interview", "Interview"),
                            ("offered", "Offered"),
                            ("hired", "Hired"),
                            ("rejected", "Rejected"),
                        ],
                        db_index=True,
                        default="applied",
                        max_length=16,
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="applications", to="recruitment.candidate"),
                ),
                (
                    "opening",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="applications", to="recruitment.jobopening"),
                ),
            ],
        ),
    ]
