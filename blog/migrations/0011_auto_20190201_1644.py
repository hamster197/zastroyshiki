# Generated by Django 2.1.2 on 2019-02-01 13:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190201_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_hod_st',
            name='pict1',
            field=models.ImageField(blank=True, upload_to='image/hodst', verbose_name='Фото объекта №1'),
        ),
        migrations.AlterField(
            model_name='blog_hod_st',
            name='pict2',
            field=models.ImageField(blank=True, upload_to='image/hodst', verbose_name='Фото объекта №2'),
        ),
        migrations.AlterField(
            model_name='blog_hod_st',
            name='pict3',
            field=models.ImageField(blank=True, upload_to='image/hodst', verbose_name='Фото объекта №3'),
        ),
        migrations.AlterField(
            model_name='blog_hod_st',
            name='pict4',
            field=models.ImageField(blank=True, upload_to='image/hodst', verbose_name='Фото объекта №4'),
        ),
        migrations.AlterField(
            model_name='blog_hod_st',
            name='text',
            field=tinymce.models.HTMLField(max_length=865, verbose_name='Oписание:'),
        ),
    ]
