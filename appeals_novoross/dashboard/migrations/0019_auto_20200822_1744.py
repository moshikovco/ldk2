# Generated by Django 3.1 on 2020-08-22 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20200822_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='apealscomments',
            name='type',
            field=models.IntegerField(choices=[(0, 'Системное сообщение'), (1, 'Сообщение')], default=1),
        ),
        migrations.AlterField(
            model_name='apeals',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 17, 44, 44, 640596)),
        ),
        migrations.AlterField(
            model_name='apealscomments',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 17, 44, 44, 641173)),
        ),
    ]
