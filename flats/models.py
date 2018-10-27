from django.core.validators import MinValueValidator
from django.db import models



class Planirovki(models.Model):
    pl_name = models.CharField(max_length=40, default='',verbose_name='Название планировки:')
    corp_name_choise = (('1 корпус','1 корпус'),('2 корпус','2 корпус'))
    corp_name = models.CharField(max_length=25, verbose_name=' Корпус:', default='', choices=corp_name_choise)
    pinct = models.ImageField(verbose_name='Планировка квартиры:', upload_to='image', default='')
    def __str__(self):
        return self.pl_name
    class Meta:
        verbose_name = 'Планировка'
        verbose_name_plural = 'Планировки'

class flat(models.Model):
    korpus_choises = (('Выберите корпус','Выберите корпус'),('1 корпус','1 корпус'),('2 корпус','2 корпус'),
                      ('3 корпус','3 корпус'))
    korpus = models.CharField(max_length=20, verbose_name='Корпус:', choices=korpus_choises, default='')
    etag_choises = (('Выберите этаж','Выберите этаж'),('1 Этаж','1 Этаж'),('2 Этаж','2 Этаж'),('3 Этаж','3 Этаж'),
                    ('4 Этаж','4 Этаж'),('5 Этаж', '5 Этаж'), ('6 Этаж', '6 Этаж'), ('7 Этаж', '7 Этаж'),
                    ('8 Этаж', '8 Этаж'))
    etag = models.CharField(max_length=15,verbose_name='Этаж:', choices=etag_choises, default='')
    komn_choises=(('Выберите','Выберите'),('Студия','Студия'),('Однокомнатная','Однокомнатная'),('Двухкомнатная','Двухкомнатная'),
                  ('Трехкомнатная','Трехкомнатная'),('Многокомнатная','Многокомнатная'))
    komnat=models.CharField('Кол-во комнат', max_length=25, choices=komn_choises, default='')
    kv_numb = models.CharField(max_length=5, verbose_name='№ квартиры:', default='')
    metrag = models.FloatField(verbose_name='Метраж квартиры:', default=0,validators=[MinValueValidator(7)])
    cena_za_metr = models.IntegerField(verbose_name='Цена за метр:', default=0,validators=[MinValueValidator(10000)])
    vid_choises = (('на горы','на горы'),('на горы и море','на горы и море'),('на море и город','на море и город'),
                   ('на парк','на парк'),('во двор','во двор'))
    vid = models.CharField(max_length=40, verbose_name='Вид:', choices=vid_choises, default='')
    status_choises = (('Свободна','Свободна'),('Бронь','Бронь'),('Продана','Продана'))
    status = models.CharField(max_length=25, verbose_name='Статус:',choices=status_choises, default='Свободна')
    canal_prodagi_choises = (('Агенство','Агенство'),('Частный риелтор','Частный риелтор'),
                              ('Прямая продажа','Прямая продажа'))
    canal_prodagi = models.CharField(max_length=35, verbose_name='Канал продажи:', choices=canal_prodagi_choises,
                                     default='')
    planirovka = models.ForeignKey(Planirovki, verbose_name='Планировка квартиры:', on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.kv_numb
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'




