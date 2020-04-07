# Generated by Django 3.0.4 on 2020-03-22 23:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0008_auto_20200323_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agreement',
            name='id_negotiator',
        ),
        migrations.AlterField(
            model_name='agreement',
            name='period_finish',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 1, 21, 39, 899469), verbose_name='Finish period of agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='period_start',
            field=models.DateField(default=datetime.datetime(2020, 3, 22, 23, 21, 39, 899469, tzinfo=utc), verbose_name='Start period of agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsible person'),
        ),
    ]