# Generated by Django 4.2.9 on 2024-03-19 12:59

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Neighborhood",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("discord_role_id", models.CharField(blank=True, max_length=64, null=True)),
                ("discord_channel_id", models.CharField(blank=True, max_length=64, null=True)),
                ("approved", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=512)),
            ],
        ),
    ]
