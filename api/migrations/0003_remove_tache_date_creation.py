# Generated by Django 5.0.3 on 2024-03-19 11:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_tache_date_creation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tache",
            name="date_creation",
        ),
    ]
