# Generated by Django 4.2.2 on 2024-03-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0014_alter_appointment_options_alter_appointment_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(),
        ),
    ]
