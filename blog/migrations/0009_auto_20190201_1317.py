# Generated by Django 2.1.2 on 2019-02-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190201_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_hod_st',
            name='date_sozd',
            field=models.DateField(verbose_name='Дата создания:'),
        ),
    ]
