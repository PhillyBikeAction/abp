# Generated by Django 4.2.9 on 2024-03-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0006_campaign_events"),
    ]

    operations = [
        migrations.AddField(
            model_name="petition",
            name="call_to_action",
            field=models.CharField(
                blank=True,
                default="Add your signature to the following message",
                max_length=64,
                null=True,
            ),
        ),
    ]
