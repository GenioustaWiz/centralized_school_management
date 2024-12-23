# Generated by Django 5.1 on 2024-10-12 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schoolcontactinfo",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact_info",
                to="schools.school",
            ),
        ),
    ]
