# Generated by Django 3.0.4 on 2020-03-22 23:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20200322_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='period_finish',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 19, 59, 712532), verbose_name='Finish period of agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='period_start',
            field=models.DateField(default=datetime.datetime(2020, 3, 22, 23, 19, 59, 712532, tzinfo=utc), verbose_name='Start period of agreement'),
        ),
    ]
