# Generated by Django 4.2.9 on 2024-03-22 13:53

import uuid

import markdownfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=512)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("completed", "Completed"),
                            ("canceled", "Canceled"),
                            ("suspended", "Suspended"),
                            ("unknown", "Unknown"),
                        ],
                        max_length=16,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("cover", models.URLField(blank=True, null=True)),
                ("content", markdownfield.models.MarkdownField(rendered_field="content_rendered")),
                ("content_rendered", markdownfield.models.RenderedMarkdownField()),
            ],
        ),
    ]
