# Generated by Django 3.1 on 2020-08-21 20:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='addres',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='subject',
            name='addres_arr',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='subject',
            name='gender',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='first_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='last_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='midle_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Отчество'),
        ),
    ]