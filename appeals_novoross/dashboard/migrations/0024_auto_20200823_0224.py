# Generated by Django 3.1 on 2020-08-22 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20200823_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apeals',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 2, 24, 38, 308776)),
        ),
        migrations.AlterField(
            model_name='apeals',
            name='uid',
            field=models.CharField(default='ZQhXARZ2', max_length=16),
        ),
        migrations.AlterField(
            model_name='apealscomments',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 2, 24, 38, 309467)),
        ),
    ]