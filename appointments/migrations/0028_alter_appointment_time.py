# Generated by Django 4.2.2 on 2024-03-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0027_appointment_duration_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='09:00'),
        ),
    ]
