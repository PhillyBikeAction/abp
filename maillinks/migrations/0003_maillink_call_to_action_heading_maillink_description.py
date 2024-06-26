# Generated by Django 4.2.13 on 2024-07-01 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maillinks", "0002_maillink_call_to_action_alter_maillink_cc"),
    ]

    operations = [
        migrations.AddField(
            model_name="maillink",
            name="call_to_action_heading",
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="maillink",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
