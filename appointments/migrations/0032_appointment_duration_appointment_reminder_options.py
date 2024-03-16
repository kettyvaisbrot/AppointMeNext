# Generated by Django 4.2.2 on 2024-03-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0031_remove_appointment_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='reminder_options',
            field=models.ManyToManyField(blank=True, to='appointments.reminderoption'),
        ),
    ]
