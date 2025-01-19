# Generated by Django 4.2.13 on 2025-01-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0010_delete_shirtinterest"),
        ("facets", "0004_statehousedistrict_statesenatedistrict"),
    ]

    operations = [
        migrations.AddField(
            model_name="district",
            name="organizers",
            field=models.ManyToManyField(
                blank=True, related_name="organizers", to="profiles.profile"
            ),
        ),
    ]
