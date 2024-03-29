# Generated by Django 4.2.9 on 2024-02-05 14:28

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ScheduledEvent",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("discord_id", models.CharField(blank=True, max_length=64, null=True)),
                ("wordpress_id", models.CharField(blank=True, max_length=64, null=True)),
                ("wordpress_slug", models.SlugField(blank=True, null=True)),
                ("title", models.CharField(max_length=512)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("scheduled", "Scheduled"),
                            ("active", "Active"),
                            ("completed", "Completed"),
                            ("canceled", "Canceled"),
                            ("deleted", "Deleted"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=16,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("cover", models.URLField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=512, null=True)),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EventSignIn",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("mailchimp_contact_id", models.CharField(blank=True, max_length=64, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=254)),
                (
                    "council_district",
                    models.IntegerField(
                        choices=[
                            (0, "N/A - I do not live in Philadelphia"),
                            (1, "District 1"),
                            (2, "District 2"),
                            (3, "District 3"),
                            (4, "District 4"),
                            (5, "District 5"),
                            (6, "District 6"),
                            (7, "District 7"),
                            (8, "District 8"),
                            (9, "District 9"),
                            (10, "District 10"),
                        ]
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Must be a valid zipcode in formats 19107 or 19107-3200",
                                regex="^(^[0-9]{5}(?:-[0-9]{4})?$|^$)",
                            )
                        ],
                    ),
                ),
                ("newsletter_opt_in", models.BooleanField(default=False)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.scheduledevent"
                    ),
                ),
            ],
        ),
    ]
