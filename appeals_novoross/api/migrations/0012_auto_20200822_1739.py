# Generated by Django 3.1 on 2020-08-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200822_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalform',
            name='uid',
            field=models.CharField(default='YRw14T4chatZkywwW2NzebEnQGiOPE1t', max_length=32),
        ),
    ]