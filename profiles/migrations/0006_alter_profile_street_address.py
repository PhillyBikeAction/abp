# Generated by Django 4.2.13 on 2024-09-01 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0005_street_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="street_address",
            field=models.CharField(
                blank=True,
                help_text=(
                    "Your Street Address. "
                    "We use this to connect you with actions "
                    "you can make in your neighborhood."
                ),
                max_length=256,
                null=True,
                verbose_name="Street Address",
            ),
        ),
    ]