# Generated by Django 3.0.4 on 2020-03-22 19:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0005_auto_20200322_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='period_finish',
            field=models.DateField(default=datetime.datetime(2020, 4, 22, 21, 36, 45, 186107), verbose_name='Finish period of agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='period_start',
            field=models.DateField(default=datetime.datetime(2020, 3, 22, 21, 36, 45, 186107), verbose_name='Start period of agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
