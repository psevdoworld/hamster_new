# Generated by Django 5.1.1 on 2024-10-19 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_code_execution_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Homework",
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
                ("fairy_tale", models.TextField(blank=True, default="")),
            ],
        ),
        migrations.CreateModel(
            name="Solution",
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
                ("text", models.TextField(blank=True, default="")),
                ("score", models.FloatField(default=0.0)),
                ("log", models.TextField(blank=True, default="")),
            ],
        ),
        migrations.CreateModel(
            name="Example",
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
                ("input", models.TextField(blank=True, default="")),
                ("output", models.TextField(blank=True, default="")),
                (
                    "hw",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.homework"
                    ),
                ),
            ],
        ),
    ]
