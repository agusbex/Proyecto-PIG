# Generated by Django 5.0 on 2024-07-03 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_logentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogEntry',
        ),
    ]
