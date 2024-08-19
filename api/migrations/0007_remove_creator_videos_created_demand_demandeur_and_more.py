# Generated by Django 4.1.2 on 2024-06-25 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0006_remove_creator_video_link_video"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="creator",
            name="videos_created",
        ),
        migrations.AddField(
            model_name="demand",
            name="demandeur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="demandeur",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos_created",
                to="api.creator",
            ),
        ),
    ]
