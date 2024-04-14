# Generated by Django 4.2.2 on 2024-03-12 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0025_appointment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='reminder_options',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='receive_reminders',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='reminder_options',
        ),
        migrations.DeleteModel(
            name='ReminderOption',
        ),
    ]