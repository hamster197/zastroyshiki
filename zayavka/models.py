from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class zayavka(models.Model):
    date_sozd = models.DateField(verbose_name='Дата создания:')
    date_vz = models.DateField(verbose_name='Дата взятия в работу:', null=True, blank=True)
    date_zakr = models.DateField(verbose_name='Дата закрытия заявки:', null=True, blank=True)
    kanal_pr_choises = (('Авито','Авито'),('Домклик','Домклик'),('Яндекс','Яндекс'),('Циан','Циан'),
                        ('Тел.Звонок','Тел.Звонок'),('Разное','Разное'),('Заявка с сайта','Заявка с сайта'))
    kanal_pr = models.CharField(max_length=35,verbose_name='Источник заявки:')
    name_kl = models.CharField(max_length=55, verbose_name='Имя клиента:', help_text='Имя')
    tel = PhoneNumberField(verbose_name='Телефон:',help_text='Ваш номер телефона:')
    text = models.TextField(verbose_name='Описание заявки:')
    status_ch = (('Новая заявка','Новая заявка'),('В работе','В работе'),('Сделка','Сделка'),('Отказ','Отказ'))
    status = models.CharField(verbose_name='Статус заявки:', max_length=35, choices=status_ch)
    comment = models.TextField(verbose_name='Комментарий')
    pr_prizn_choise = (('Да','Да'),('Нет','Нет'))
    prizn_pr = models.CharField(max_length=3, verbose_name='Признак просмотра', default='Нет' )
    ##################################
    ## Info about Flat
    ##################################
    corpus = models.CharField(verbose_name='Корпус:', max_length=55,default='')
    comnat = models.CharField(verbose_name='Кол-во комнат:',max_length=55,default='')
    ploshad = models.CharField(verbose_name='Площадь квартиры:', default=0, max_length=55)
    kv_numb = models.CharField(verbose_name='№ квартиры', default=0, max_length=55)
    stoimost = models.IntegerField(verbose_name='Стоимость квартиры:', default=0)
    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
    def __str__(self):
        return str(self.tel)