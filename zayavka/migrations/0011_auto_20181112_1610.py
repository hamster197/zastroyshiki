# Generated by Django 2.1.2 on 2018-11-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayavka', '0010_zayavka_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]