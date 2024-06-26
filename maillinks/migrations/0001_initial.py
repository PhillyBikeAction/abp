# Generated by Django 4.2.13 on 2024-07-01 20:33

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MailLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=512)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("active", models.BooleanField(default=False)),
                ("to", models.CharField(max_length=1024)),
                ("cc", models.CharField(max_length=1024)),
                ("subject", models.CharField(max_length=512)),
                ("body", models.TextField()),
            ],
        ),
    ]
