# Generated by Django 3.0.4 on 2020-03-22 23:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20200323_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agreement',
            name='period_finish',
        ),
        migrations.RemoveField(
            model_name='agreement',
            name='period_start',
        ),
        migrations.CreateModel(
            name='Periods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField(default=datetime.datetime(2020, 3, 22, 23, 42, 14, 753510, tzinfo=utc), verbose_name='Start period of agreement')),
                ('period_finish', models.DateField(default=datetime.datetime(2020, 4, 23, 1, 42, 14, 753510), verbose_name='Finish period of agreement')),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Agreement', verbose_name='Discount Agreement')),
            ],
            options={
                'verbose_name': 'periods',
                'verbose_name_plural': 'periods',
            },
        ),
    ]
