from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("name", models.CharField(max_length=120, unique=True)),
                ("code", models.CharField(db_index=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="JobRole",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, db_index=True, null=True)),
                ("title", models.CharField(db_index=True, max_length=140)),
                ("description", models.TextField(blank=True)),
                (
                    "department",
                    models.ForeignKey(on_delete=models.deletion.PROTECT, related_name="roles", to="organization.department"),
                ),
            ],
            options={"unique_together": {("title", "department")}},
        ),
    ]
