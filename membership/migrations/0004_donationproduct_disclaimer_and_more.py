# Generated by Django 4.2.13 on 2024-11-23 21:57

import django.db.models.deletion
import markdownfield.models
from django.db import migrations, models

import pbaabp.models


class Migration(migrations.Migration):

    dependencies = [
        ("membership", "0003_donation"),
    ]

    operations = [
        migrations.AddField(
            model_name="donationproduct",
            name="disclaimer",
            field=pbaabp.models.MarkdownField(
                blank=True, null=True, rendered_field="disclaimer_rendered"
            ),
        ),
        migrations.AddField(
            model_name="donationproduct",
            name="disclaimer_rendered",
            field=markdownfield.models.RenderedMarkdownField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="donation",
            name="donation_product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="donations",
                to="membership.donationproduct",
            ),
        ),
    ]
