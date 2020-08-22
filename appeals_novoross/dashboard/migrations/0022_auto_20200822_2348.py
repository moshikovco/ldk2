# Generated by Django 3.1 on 2020-08-22 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20200822_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apeals',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 23, 48, 58, 198628)),
        ),
        migrations.AlterField(
            model_name='apeals',
            name='format',
            field=models.IntegerField(choices=[(0, 'froms'), (1, 'email'), (2, 'phone')], default=0),
        ),
        migrations.AlterField(
            model_name='apealscomments',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 23, 48, 58, 199205)),
        ),
    ]
