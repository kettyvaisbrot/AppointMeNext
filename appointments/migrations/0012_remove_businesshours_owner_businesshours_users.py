# Generated by Django 4.2.2 on 2024-03-02 08:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_alter_businesshours_friday_close_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesshours',
            name='owner',
        ),
        migrations.AddField(
            model_name='businesshours',
            name='users',
            field=models.ManyToManyField(related_name='business_hours', to=settings.AUTH_USER_MODEL),
        ),
    ]