# Generated by Django 5.1.2 on 2024-11-26 06:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0002_rename_status_habitlog_statuses"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habitlog",
            old_name="statuses",
            new_name="status",
        ),
    ]
