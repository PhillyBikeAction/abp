# Generated by Django 4.2.13 on 2024-07-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0013_campaign_call_to_action_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="campaign",
            options={"ordering": ("order",)},
        ),
        migrations.AddField(
            model_name="campaign",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=1, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
    ]
