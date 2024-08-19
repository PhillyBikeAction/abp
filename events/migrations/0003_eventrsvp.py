# Generated by Django 4.2.13 on 2024-08-19 00:40

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0002_alter_scheduledevent_wordpress_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventRSVP",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=64, null=True)),
                ("last_name", models.CharField(blank=True, max_length=64, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.scheduledevent"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_rsvps",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]