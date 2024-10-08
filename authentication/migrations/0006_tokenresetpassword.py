# Generated by Django 4.1.2 on 2024-03-15 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0005_user_company_start_date_user_entity_start_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="TokenResetPassword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token", models.UUIDField(default=uuid.uuid4)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("expiration_date", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
