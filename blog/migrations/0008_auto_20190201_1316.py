# Generated by Django 2.1.2 on 2019-02-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190201_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_hod_st',
            name='date_sozd',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания:'),
        ),
    ]
