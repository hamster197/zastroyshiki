# Generated by Django 2.1.2 on 2018-11-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayavka', '0002_auto_20181108_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavka',
            name='corpus',
            field=models.CharField(default='', max_length=55, verbose_name='Корпус:'),
        ),
    ]
