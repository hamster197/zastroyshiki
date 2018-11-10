# Generated by Django 2.1.2 on 2018-11-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayavka', '0007_auto_20181110_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='kanal_pr',
            field=models.CharField(choices=[('Авито', 'Авито'), ('Домклик', 'Домклик'), ('Яндекс', 'Яндекс'), ('Циан', 'Циан'), ('Тел.Звонок', 'Тел.Звонок'), ('Разное', 'Разное'), ('Заявка с сайта', 'Заявка с сайта')], max_length=35, verbose_name='Источник заявки:'),
        ),
    ]
