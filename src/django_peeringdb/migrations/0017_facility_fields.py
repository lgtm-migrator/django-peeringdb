# Generated by Django 3.2.7 on 2021-09-07 13:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_inet.models
import django_peeringdb.fields
import django_peeringdb.models.abstract


class Migration(migrations.Migration):

    dependencies = [
        ("django_peeringdb", "0016_add_ix_service_and_terms"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="available_voltage_services",
            field=django_peeringdb.fields.MultipleChoiceField(
                blank=True,
                choices=[
                    ("48 VDC", "48 VDC"),
                    ("120 VAC", "120 VAC"),
                    ("208 VAC", "208 VAC"),
                    ("240 VAC", "240 VAC"),
                    ("480 VAC", "480 VAC"),
                ],
                help_text="The alternating current voltage available to users of the facility either directly from the landlord or delivered by the utility separately.",
                max_length=255,
                null=True,
                verbose_name="Available Voltage Services",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="diverse_serving_substations",
            field=models.BooleanField(
                blank=True,
                help_text="Two separate and distinct paths to individual substations which should maintain a separated path back to one or more utility generator stations.",
                null=True,
                verbose_name="Diverse Serving Substations",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="property",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Owner", "Owner"),
                    ("Lessee", "Lessee"),
                ],
                help_text="A property owner is the individual or entity that has title to the property. A lessee is a user of a property who has a lease, an agreement, with the owner of the property.",
                max_length=27,
                null=True,
                verbose_name="Property",
            ),
        ),
    ]
