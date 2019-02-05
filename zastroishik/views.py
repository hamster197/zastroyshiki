from datetime import datetime, timedelta

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

import blog
from blog.models import stavki_ip
from flats.models import flat, agenstv_spr
from zastroishik.forms import loginform, SdelkiDateForm
from zayavka.forms import zayavkaFromSaitForm
from zayavka.models import zayavka


def loginView(request):
    if request.POST:
        form = loginform(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['username']
            psw = form.cleaned_data['passw']
            user = authenticate(username = usr , password = psw)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('mainpage')
    else:
        form = loginform()
    return render(request,'main/login.html',{'tpform':form})

def logoutView(request):
    logout(request)
    return render(request,'main/index.html')

def mainPageView(request):
    if request.POST:
        form = zayavkaFromSaitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_sozd = datetime.now()
            post.kanal_pr = 'Заявка с сайта'
            post.status = 'Новая заявка'
            ss = 'От ' + post.name_kl +' тел.'+str(post.tel)
            send_mail('Поступила новая заявка на сайт', ss , 'zhem-otchet@mail.ru',
                      ['sawf@rambler.ru'], fail_silently=False, html_message=ss)
            post.save()
    else:
        form = zayavkaFromSaitForm()
    return render(request,'main/index.html',{'tpForm':form})

def AboutPageView(request):
    return render(request,'main/about.html')

def HodStroitPageView(request):
    return render(request,'main/hodstroy.html')

def DokumentsPageView(request):
    return render(request,'main/doki.html')

def ContactsPageView(request):
    if request.POST:
        form = zayavkaFromSaitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_sozd = datetime.now()
            post.kanal_pr = 'Заявка с сайта'
            post.status = 'Новая заявка'
            post.save()
            ss = 'От ' + post.name_kl +' тел.'+str(post.tel)
            send_mail('Поступила новая заявка на сайт', ss , 'zhem-otchet@mail.ru',
                      ['hamster197@mail.ru'], fail_silently=False, html_message=ss)
    else:
        form = zayavkaFromSaitForm()
    return render(request,'main/contacts.html',{'tpForm':form})

def IpotecaPageView(request):
    st = get_object_or_404(stavki_ip, pk=1)
    return render(request,'main/ipoteca.html',{'st':st})

def FZ214PageView(request):
    return render(request,'main/fz214.html')

def RasrochkaPageView(request):
    return render(request,'main/rasr.html')

def RemontPageView(request):
    return render(request,'main/remon.html')

def PoliticaConfPageView(request):
    return render(request,'main/Politicakonf.html')

@login_required
def SdekaAnView(request):
    if request.POST:
        a = ''
        form = SdelkiDateForm(request.POST)
        if form.is_valid():
            a= ''
            ds = form.cleaned_data['date_st']
            de = form.cleaned_data['date_end']
    else:
        a = ''
        form = SdelkiDateForm(
            initial={'date_st': datetime.now().date() - timedelta(days=datetime.now().day) + timedelta(days=1),
                     'date_end': datetime.now()})
        ds = datetime.now().date()-timedelta(days=datetime.now().day)+timedelta(days=1)
        de = datetime.now()
    sdelki = flat.objects.filter(status='Продана', sdelka_date__gte=ds,
                                         sdelka_date__lte= de).order_by('-sdelka_date')
    bron = flat.objects.filter(status='Бронь').order_by('-bron_date_end')

    return render(request,'main/sdelkiStat.html', {'tform':form,'tsdelki':sdelki,'tbron':bron, 'a':a})


@login_required
def AnaliticaView(request):
    all_kv = flat.objects.all().count()
    all_bron_kv = flat.objects.filter(status='Бронь').count()
    all_prodano_kv = flat.objects.filter(status='Продана').count()
    one_korp_prod_kvart = flat.objects.filter(status='Продана', korpus='1 корпус').count()
    one_korp_bron_kvart = flat.objects.filter(status='Бронь', korpus='1 корпус').count()
    one_korp_sv_kvart = flat.objects.filter(status='Свободна', korpus='1 корпус').count()
    two_korp_prod_kvart = flat.objects.filter(status='Продана', korpus='2 корпус').count()
    two_korp_bron_kvart = flat.objects.filter(status='Бронь', korpus='2 корпус').count()
    two_korp_sv_kvart = flat.objects.filter(status='Свободна', korpus='2 корпус').count()

    one_korp_prod_st_all = flat.objects.filter(Q (planirovka_id=1) | Q(planirovka_id=3)| Q(planirovka_id=14),
                                               korpus='1 корпус').count()
    one_korp_prod_st = flat.objects.filter(Q (planirovka_id=1) | Q(planirovka_id=3)| Q(planirovka_id=14),
                                           status='Продана', korpus='1 корпус').count()
    one_korp_prod_OneKm_all = flat.objects.filter(Q(planirovka_id=2) | Q(planirovka_id=4)| Q(planirovka_id=5)  |
                                                  Q(planirovka_id=6) | Q(planirovka_id=7) | Q(planirovka_id=11) |
                                                  Q(planirovka_id=13) | Q(planirovka_id=15) | Q(planirovka_id=16) |
                                                  Q(planirovka_id=17) | Q(planirovka_id=21) | Q(planirovka_id=22) |
                                                  Q(planirovka_id=24) | Q(planirovka_id=25) | Q(planirovka_id=26),
                                               korpus='1 корпус').count()
    one_korp_prod_OneKm = flat.objects.filter(Q(planirovka_id=2) | Q(planirovka_id=4)| Q(planirovka_id=5)  |
                                                  Q(planirovka_id=6) | Q(planirovka_id=7) | Q(planirovka_id=11) |
                                                  Q(planirovka_id=13) | Q(planirovka_id=15) | Q(planirovka_id=16) |
                                                  Q(planirovka_id=17) | Q(planirovka_id=21) | Q(planirovka_id=22) |
                                                  Q(planirovka_id=24) | Q(planirovka_id=25) | Q(planirovka_id=26),
                                           status='Продана', korpus='1 корпус').count()
    one_korp_prod_TwoKm_all = flat.objects.filter(Q (planirovka_id=12) | Q(planirovka_id=18)|Q(planirovka_id=20)|
                                                  Q(planirovka_id=23), korpus='1 корпус').count()
    one_korp_prod_TwoKm = flat.objects.filter(Q (planirovka_id=12) | Q(planirovka_id=18)| Q(planirovka_id=20)|
                                              Q(planirovka_id=23), status='Продана', korpus='1 корпус').count()
    one_korp_prod_ThreKm_all = flat.objects.filter(Q (planirovka_id=8) | Q(planirovka_id=9)|Q(planirovka_id=10)|
                                                  Q(planirovka_id=19), korpus='1 корпус').count()
    one_korp_prod_ThreKm = flat.objects.filter(Q (planirovka_id=8) | Q(planirovka_id=9)| Q(planirovka_id=10)|
                                              Q(planirovka_id=19), status='Продана', korpus='1 корпус').count()

    two_korp_prod_st_all = flat.objects.filter(Q (planirovka_id=1) | Q(planirovka_id=3)| Q(planirovka_id=14),
                                               korpus='2 корпус').count()
    two_korp_prod_st = flat.objects.filter(Q (planirovka_id=1) | Q(planirovka_id=3)| Q(planirovka_id=14),
                                           status='Продана', korpus='2 корпус').count()
    two_korp_prod_OneKm_all = flat.objects.filter(Q(planirovka_id=2) | Q(planirovka_id=4)| Q(planirovka_id=5)  |
                                                  Q(planirovka_id=6) | Q(planirovka_id=7) | Q(planirovka_id=11) |
                                                  Q(planirovka_id=13) | Q(planirovka_id=15) | Q(planirovka_id=16) |
                                                  Q(planirovka_id=17) | Q(planirovka_id=21) | Q(planirovka_id=22) |
                                                  Q(planirovka_id=24) | Q(planirovka_id=25) | Q(planirovka_id=26),
                                               korpus='2 корпус').count()
    two_korp_prod_OneKm = flat.objects.filter(Q(planirovka_id=2) | Q(planirovka_id=4)| Q(planirovka_id=5)  |
                                                  Q(planirovka_id=6) | Q(planirovka_id=7) | Q(planirovka_id=11) |
                                                  Q(planirovka_id=13) | Q(planirovka_id=15) | Q(planirovka_id=16) |
                                                  Q(planirovka_id=17) | Q(planirovka_id=21) | Q(planirovka_id=22) |
                                                  Q(planirovka_id=24) | Q(planirovka_id=25) | Q(planirovka_id=26),
                                           status='Продана', korpus='2 корпус').count()
    two_korp_prod_TwoKm_all = flat.objects.filter(Q (planirovka_id=12) | Q(planirovka_id=18)|Q(planirovka_id=20)|
                                                  Q(planirovka_id=23), korpus='2 корпус').count()
    two_korp_prod_TwoKm = flat.objects.filter(Q (planirovka_id=12) | Q(planirovka_id=18)| Q(planirovka_id=20)|
                                              Q(planirovka_id=23), status='Продана', korpus='2 корпус').count()
    two_korp_prod_ThreKm_all = flat.objects.filter(Q (planirovka_id=8) | Q(planirovka_id=9)|Q(planirovka_id=10)|
                                                  Q(planirovka_id=19), korpus='2 корпус').count()
    two_korp_prod_ThreKm = flat.objects.filter(Q (planirovka_id=8) | Q(planirovka_id=9)| Q(planirovka_id=10)|
                                              Q(planirovka_id=19), status='Продана', korpus='1 корпус').count()
    sdelka_razn_kn = flat.objects.filter(status='Продана', kanal_pr='Разное').count()
    sdelka_av_kn = flat.objects.filter(status='Продана', kanal_pr='Авито').count()
    sdelka_dm_kn = flat.objects.filter(status='Продана', kanal_pr='Домклик').count()
    sdelka_ya_kn = flat.objects.filter(status='Продана', kanal_pr='Яндекс').count()
    sdelka_cian_kn = flat.objects.filter(status='Продана', kanal_pr='Циан').count()
    sdelka_tel_kn = flat.objects.filter(status='Продана', kanal_pr='Тел.Звонок').count()
    sdelka_ag_kn = flat.objects.filter(status='Продана', kanal_pr='Агенство').count()
    sdelka_sait_kn = flat.objects.filter(status='Продана', kanal_pr='Заявка с сайта').count()

    zayav_kn_av = zayavka.objects.filter(kanal_pr='Авито').count()
    zayav_kn_dm = zayavka.objects.filter(kanal_pr='Домклик').count()
    zayav_kn_ya = zayavka.objects.filter(kanal_pr='Яндекс').count()
    zayav_kn_cian = zayavka.objects.filter(kanal_pr='Циан').count()
    zayav_kn_tel = zayavka.objects.filter(kanal_pr='Тел.Звонок').count()
    zayav_kn_raz = zayavka.objects.filter(kanal_pr='Разное').count()
    zayav_kn_sait = zayavka.objects.filter(kanal_pr='Заявка с сайта').count()

    for ag in agenstv_spr.objects.all():
        ag.kol_sdel = flat.objects.filter(agenstvo = ag.id).count()
        ag.save()
    ag = agenstv_spr.objects.all()[:10]

    return render(request, 'main/analitica.html',{'tAllKv':all_kv,'tall_bron_kv':all_bron_kv,'tall_prodano_kv':all_prodano_kv,
                                                  'one_korp_prod_kvart':one_korp_prod_kvart,
                                                  'one_korp_bron_kvart':one_korp_bron_kvart,'one_korp_sv_kvart':one_korp_sv_kvart,
                                                  'two_korp_prod_kvart': two_korp_prod_kvart,
                                                  'two_korp_bron_kvart': two_korp_bron_kvart,
                                                  'two_korp_sv_kvart': two_korp_sv_kvart,
                                                  'one_korp_prod_st_all':one_korp_prod_st_all,'one_korp_prod_st':one_korp_prod_st,
                                                  'one_korp_prod_OneKm_all':one_korp_prod_OneKm_all,'one_korp_prod_OneKm':one_korp_prod_OneKm,
                                                  'one_korp_prod_TwoKm_all':one_korp_prod_TwoKm_all,'one_korp_prod_TwoKm':one_korp_prod_TwoKm,
                                                  'one_korp_prod_ThreKm_all':one_korp_prod_ThreKm_all, 'one_korp_prod_ThreKm':one_korp_prod_ThreKm,
                                                  'two_korp_prod_st_all': two_korp_prod_st_all,'two_korp_prod_st': two_korp_prod_st,
                                                  'two_korp_prod_OneKm_all': two_korp_prod_OneKm_all,'two_korp_prod_OneKm': two_korp_prod_OneKm,
                                                  'two_korp_prod_TwoKm_all': two_korp_prod_TwoKm_all, 'two_korp_prod_TwoKm': two_korp_prod_TwoKm,
                                                  'two_korp_prod_ThreKm_all': two_korp_prod_ThreKm_all, 'two_korp_prod_ThreKm': two_korp_prod_ThreKm,
                                                  'sdelka_razn_kn':sdelka_razn_kn,'sdelka_av_kn':sdelka_av_kn,'sdelka_dm_kn':sdelka_dm_kn,
                                                  'sdelka_ya_kn':sdelka_ya_kn,'sdelka_cian_kn':sdelka_cian_kn,'sdelka_tel_kn':sdelka_tel_kn,
                                                  'sdelka_ag_kn':sdelka_ag_kn,'sdelka_sait_kn':sdelka_sait_kn,
                                                  'zayav_kn_av':zayav_kn_av,'zayav_kn_dm':zayav_kn_dm,'zayav_kn_ya':zayav_kn_ya,
                                                  'zayav_kn_cian':zayav_kn_cian,'zayav_kn_tel':zayav_kn_tel,
                                                  'zayav_kn_raz':zayav_kn_raz,'zayav_kn_sait':zayav_kn_sait,'tag':ag,
                                                  })


