# Generated by Django 5.1.1 on 2024-10-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="code",
            name="text",
            field=models.TextField(default=""),
        ),
    ]
