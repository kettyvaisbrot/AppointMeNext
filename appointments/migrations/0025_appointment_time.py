# Generated by Django 4.2.2 on 2024-03-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0024_remove_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='09:00:00'),
            preserve_default=False,
        ),
    ]
