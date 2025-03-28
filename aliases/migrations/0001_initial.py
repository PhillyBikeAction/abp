# Generated by Django 4.2.13 on 2025-02-12 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "alias",
                    models.CharField(
                        help_text="The alias name, the part before the @", max_length=64
                    ),
                ),
                (
                    "domain",
                    models.CharField(
                        default="bikeaction.org",
                        help_text="The domain, the part after the @",
                        max_length=64,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="A description for humans.",
                        max_length=128,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("mailgun_id", models.CharField(blank=True, max_length=64, null=True)),
                ("mailgun_updated_at", models.DateTimeField(null=True)),
            ],
            options={
                "verbose_name_plural": "aliases",
            },
        ),
        migrations.CreateModel(
            name="AliasRecipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("email_address", models.EmailField(max_length=254)),
                (
                    "alias",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipients",
                        to="aliases.alias",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="aliasrecipient",
            constraint=models.UniqueConstraint(
                models.F("alias"), models.F("email_address"), name="unique_emails_per_alias"
            ),
        ),
    ]
