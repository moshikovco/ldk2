# Generated by Django 3.1 on 2020-08-22 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20200822_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apeals',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 22, 15, 46, 43, 11911)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='email',
            field=models.EmailField(blank=True, max_length=128, null=True, verbose_name='Email'),
        ),
    ]
