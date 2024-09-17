# Generated by Django 5.1 on 2024-08-31 06:36

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("parents", "0001_initial"),
        ("schools", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "Emergency_contact",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("enrollment_date", models.DateTimeField(auto_now_add=True)),
                ("school_identification", models.CharField(max_length=20, unique=True)),
                (
                    "student_number",
                    models.CharField(editable=False, max_length=10, unique=True),
                ),
                ("rfid_tag", models.CharField(max_length=20, unique=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="parents.parent",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schools.school"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Performance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=50)),
                ("grade", models.FloatField()),
                ("assessment_date", models.DateField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Present", "Present"),
                            ("Absent", "Absent"),
                            ("Late", "Late"),
                            ("Excused", "Excused"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                    ),
                ),
            ],
        ),
    ]
