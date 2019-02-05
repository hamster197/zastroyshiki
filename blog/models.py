#from tinymce.models import HTMLField
from django.db import models
#from django.utils import timezone

class stavki_ip(models.Model):
    sber_proc = models.FloatField(verbose_name='Процентная ставка(Сбербанк):', blank=False, default=0)
    sber_vznos = models.IntegerField(verbose_name='Первый взнос(Сбербанк):', blank=False, default=0)
    sber_srok = models.IntegerField(verbose_name='Срок кредита:(Сбербанк)', blank=False, default=0)

    vtb_proc = models.FloatField(verbose_name='Процентная ставка(BTБ):', blank=False, default=0)
    vtb_vznos = models.IntegerField(verbose_name='Первый взнос(BTБ):', blank=False, default=0)
    vtb_srok = models.IntegerField(verbose_name='Срок кредита(BTБ):', blank=False, default=0)

    alfa_proc = models.FloatField(verbose_name='Процентная ставка(Альфа-Банк):', blank=False, default=0)
    alfa_vznos = models.IntegerField(verbose_name='Первый взнос(Альфа-Банк):', blank=False, default=0)
    alfa_srok = models.IntegerField(verbose_name='Срок кредита(Альфа-Банк):', blank=False, default=0)

    gaz_proc = models.FloatField(verbose_name='Процентная ставка(ГазПромБанк):', blank=False, default=0)
    gaz_vznos = models.IntegerField(verbose_name='Первый взнос(ГазПромБанк):', blank=False, default=0)
    gaz_srok = models.IntegerField(verbose_name='Срок кредита(ГазПромБанк):', blank=False, default=0)

    prom_proc = models.FloatField(verbose_name='Процентная ставка(ПромсвязьБанк):', blank=False, default=0)
    prom_vznos = models.IntegerField(verbose_name='Первый взнос(ПромсвязьБанк):', blank=False, default=0)
    prom_srok = models.IntegerField(verbose_name='Срок кредита(ПромсвязьБанк):', blank=False, default=0)

    sel_proc = models.FloatField(verbose_name='Процентная ставка(РоссельхозБанк):', blank=False, default=0)
    sel_vznos = models.IntegerField(verbose_name='Первый взнос(РоссельхозБанк):', blank=False, default=0)
    sel_srok = models.IntegerField(verbose_name='Срок кредита(РоссельхозБанк):', blank=False, default=0)

    class Meta:
        verbose_name = 'Условия кредитования'
        verbose_name_plural = 'Условия кредитования'


class blog_hod_st(models.Model):
    date_sozd = models.DateField(verbose_name='Дата создания:', null=False,)#default=timezone.now())
    nazv = models.CharField(verbose_name='Название:', max_length=65, blank=False)
    text = models.TextField(verbose_name='Oписание:', max_length=865, blank=False)
    pict1 = models.ImageField(verbose_name='Фото объекта №1', upload_to='image/hodst', blank=True)
    pict2 = models.ImageField(verbose_name='Фото объекта №2', upload_to='image/hodst', blank=True)
    pict3 = models.ImageField(verbose_name='Фото объекта №3', upload_to='image/hodst', blank=True)
    pict4 = models.ImageField(verbose_name='Фото объекта №4', upload_to='image/hodst', blank=True)
    def __str__(self):
        return self.nazv
    class Meta:
        verbose_name = 'Ход строительства'
        verbose_name_plural = 'Ход строительства'

