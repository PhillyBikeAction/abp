# Generated by Django 4.2.13 on 2024-09-19 17:45

import uuid

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facets", "0002_district_targetable_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ZipCode",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("mpoly", django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ("properties", models.JSONField()),
                ("targetable", models.BooleanField(default=False)),
            ],
        ),
    ]
