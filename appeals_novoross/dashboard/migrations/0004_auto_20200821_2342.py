# Generated by Django 3.1 on 2020-08-21 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200821_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Источник')),
            ],
        ),
        migrations.AddField(
            model_name='apeals',
            name='content',
            field=models.TextField(default='Без сообщения', verbose_name='Текст обращения'),
        ),
        migrations.AddField(
            model_name='apeals',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='apeals',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 21, 23, 42, 6, 733941)),
        ),
    ]
