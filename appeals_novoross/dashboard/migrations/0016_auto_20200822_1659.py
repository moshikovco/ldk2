# Generated by Django 3.1 on 2020-08-22 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20200822_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='apeals',
            name='topic',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Тема обращения'),
        ),
        migrations.AlterField(
            model_name='apeals',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 16, 59, 20, 293884)),
        ),
    ]
