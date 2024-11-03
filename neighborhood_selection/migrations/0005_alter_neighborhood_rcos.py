# Generated by Django 4.2.13 on 2024-11-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("facets", "0004_statehousedistrict_statesenatedistrict"),
        ("neighborhood_selection", "0004_neighborhood_rcos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="neighborhood",
            name="rcos",
            field=models.ManyToManyField(blank=True, to="facets.registeredcommunityorganization"),
        ),
    ]
