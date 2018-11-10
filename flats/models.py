from django.core.validators import MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Planirovki(models.Model):
    pl_name = models.CharField(max_length=140, default='',verbose_name='Название планировки:')
    komn_choises=(('Выберите','Выберите'),('Студия','Студия'),('Однокомнатная','Однокомнатная'),('Двухкомнатная','Двухкомнатная'),
                  ('Трехкомнатная','Трехкомнатная'))
    komnat=models.CharField('Кол-во комнат', max_length=25, choices=komn_choises, default='')
    ploshad = models.FloatField(verbose_name='Площадь квартиры:', default=0,validators=[MinValueValidator(7)])
    pict = models.ImageField(verbose_name='Планировка квартиры:', upload_to='image', default='')
    def __str__(self):
        return self.pl_name
    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'Планировки'


class agenstv_spr(models.Model):
    ag_name = models.CharField(verbose_name='Название агенства:',max_length=80, default='')
    def __str__(self):
        return self.ag_name
    class Meta:
        verbose_name = 'Справочник агентсв'
        verbose_name_plural = 'Справочник агентсв'
        ordering =['ag_name']


class flat(models.Model):
    korpus_choises = (('',''),('1 корпус','1 корпус'),('2 корпус','2 корпус'))
    korpus = models.CharField(max_length=20, verbose_name='Корпус:', choices=korpus_choises, default='')
    etag_choises = (('Выберите этаж','Выберите этаж'),('1 Этаж','1 Этаж'),('2 Этаж','2 Этаж'),('3 Этаж','3 Этаж'),
                    ('4 Этаж','4 Этаж'),('5 Этаж', '5 Этаж'), ('6 Этаж', '6 Этаж'), ('7 Этаж', '7 Этаж'),
                    ('8 Этаж', '8 Этаж'), ('9 Этаж', '9 Этаж'), ('10 Этаж', '10 Этаж'), ('11 Этаж', '11 Этаж'),
                    ('12 Этаж', '12 Этаж'))
    etag = models.CharField(max_length=15,verbose_name='Этаж:', choices=etag_choises, default='', blank=False)
    kv_numb = models.CharField(max_length=5, verbose_name='№ квартиры:', default='')
    cena_za_metr = models.IntegerField(verbose_name='Цена за метр:', default=80000,validators=[MinValueValidator(10000)])
    vid_choises = (('на горы','на горы'),('на горы и море','на горы и море'),('на море и город','на море и город'),
                   ('на парк','на парк'),('во двор','во двор'))
    vid = models.CharField(max_length=40, verbose_name='Вид:', choices=vid_choises, default='')
    status_choises = (('Свободна','Свободна'),('Бронь','Бронь'),('Продана','Продана'))
    status = models.CharField(max_length=25, verbose_name='Статус:',choices=status_choises, default='Свободна')
    planirovka = models.ForeignKey(Planirovki, verbose_name='Планировка квартиры:', on_delete=models.CASCADE, default='')
    sdelka_date = models.DateField(verbose_name='Дата сделки:',blank=True, null=True)
    agenstvo = models.ManyToManyField(agenstv_spr)
    kanal_pr_choises = (('Разное','Разное'),('Авито','Авито'),('Домклик','Домклик'),('Яндекс','Яндекс'),('Циан','Циан'),
                        ('Тел.Звонок','Тел.Звонок'),('Агенство','Агенство'),('Заявка с сайта','Заявка с сайта'))
    kanal_pr = models.CharField(max_length=35,verbose_name='Источник заявки:', choices=kanal_pr_choises)
    ###############################
    #### Start For bron
    ###############################
    bron_date_start = models.DateField(verbose_name='Дата открытия брони:',blank=True,null=True)
    bron_date_end = models.DateField(verbose_name='Дата закрытия брони:', blank=True, null=True)
    bron_vneseno = models.IntegerField(verbose_name='Внесенно брони:',default=0,)
    fio_pokupatel = models.CharField(verbose_name='ФИО покупателя:', default=' ', max_length=75)
    tel_pokupatel = PhoneNumberField(verbose_name='Телефон покупателя:', default='+70000000000', help_text='+79881450000',
                                     blank=False)
    prim = models.TextField(verbose_name='Примечание;',default='',blank=False, null=False)
    ###############################
    #### End For bron
    ###############################
    def __str__(self):
        return self.kv_numb
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'




