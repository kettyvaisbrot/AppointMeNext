# Generated by Django 4.2.2 on 2024-02-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesshours',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
