# Generated by Django 4.2.13 on 2024-11-28 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_eventrsvp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="scheduledevent",
            old_name="wordpress_slug",
            new_name="slug",
        ),
        migrations.RemoveField(
            model_name="scheduledevent",
            name="wordpress_id",
        ),
    ]
