# Generated by Django 4.2.2 on 2024-03-12 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0023_appointment_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
    ]