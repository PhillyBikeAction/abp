# Generated by Django 4.2.11 on 2024-05-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("release", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="releasesignature",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="releasesignature",
            name="last_name",
        ),
        migrations.AddField(
            model_name="releasesignature",
            name="legal_name",
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
