# Generated by Django 4.2.16 on 2024-11-08 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth_day',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
