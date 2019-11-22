from datetime import datetime

from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect

# Create your views here.
from zayavka.forms import allZayvkaAdd
from zayavka.models import zayavka
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def newZayavView(request):
    if request.POST:
        form = allZayvkaAdd(request.POST)
        if form.is_valid():
            zv = form.save(commit=False)
            zv.date_sozd = datetime.now()
            zv.status = 'Новая заявка'
            zv.save()
            return redirect('allFlatsIndex')
    form = allZayvkaAdd()
    return render(request,'zayavka/new.html',{'tform':form})

@login_required
def allZayavkaView(request):
    nzayav = zayavka.objects.filter(status='Новая заявка').order_by('-date_sozd')
    nzayav_count = zayavka.objects.filter(status='Новая заявка').count()
    wzayav = zayavka.objects.filter(status='В работе').order_by('-date_sozd')
    wzayav_count = zayavka.objects.filter(status='В работе').count()
    szayav = zayavka.objects.filter(status='Сделка').order_by('-date_sozd')
    szayav_count = zayavka.objects.filter(status='Сделка').count()
    ozayav = zayavka.objects.filter(status='Отказ').order_by('-date_sozd')
    ozayav_count = zayavka.objects.filter(status='Отказ').count()
    return render(request,'zayavka/all.html',{'tnzayav':nzayav,'tnzayav_count':nzayav_count,
                                              'twzayav':wzayav,'twzayav_count':wzayav_count,'tszayav':szayav,
                                              'tszayav_count':szayav_count,'tozayav':ozayav,'tozayav_count':ozayav_count,})

@login_required
def inWorkZayavkaView(request, idd):
    nzayav = zayavka.objects.filter(status='Новая заявка').order_by('-date_sozd')
    nzayav_count = zayavka.objects.filter(status='Новая заявка').count()
    wzayav = zayavka.objects.filter(status='В работе').order_by('-date_sozd')
    wzayav_count = zayavka.objects.filter(status='В работе').count()
    szayav = zayavka.objects.filter(status='Сделка').order_by('-date_sozd')
    szayav_count = zayavka.objects.filter(status='Сделка').count()
    ozayav = zayavka.objects.filter(status='Отказ').order_by('-date_sozd')
    ozayav_count = zayavka.objects.filter(status='Отказ').count()

    zayav = get_object_or_404(zayavka, pk = idd)
    zayav.status = 'В работе'
    zayav.date_vz = datetime.now()
    zayav.save()
    return render(request,'zayavka/all.html',{'tnzayav':nzayav,'tnzayav_count':nzayav_count,
                                              'twzayav':wzayav,'twzayav_count':wzayav_count,'tszayav':szayav,
                                              'tszayav_count':szayav_count,'tozayav':ozayav,'tozayav_count':ozayav_count,})

@login_required
def SdelkaZayavkaView(request ,idd):
    nzayav = zayavka.objects.filter(status='Новая заявка').order_by('-date_sozd')
    nzayav_count = zayavka.objects.filter(status='Новая заявка').count()
    wzayav = zayavka.objects.filter(status='В работе').order_by('-date_sozd')
    wzayav_count = zayavka.objects.filter(status='В работе').count()
    szayav = zayavka.objects.filter(status='Сделка').order_by('-date_sozd')
    szayav_count = zayavka.objects.filter(status='Сделка').count()
    ozayav = zayavka.objects.filter(status='Отказ').order_by('-date_sozd')
    ozayav_count = zayavka.objects.filter(status='Отказ').count()

    zayav = get_object_or_404(zayavka, pk = idd)
    zayav.status = 'Сделка'
    zayav.date_zakr = datetime.now()
    zayav.save()
    return render(request,'zayavka/all.html',{'tnzayav':nzayav,'tnzayav_count':nzayav_count,
                                              'twzayav':wzayav,'twzayav_count':wzayav_count,'tszayav':szayav,
                                              'tszayav_count':szayav_count,'tozayav':ozayav,'tozayav_count':ozayav_count,})

@login_required
def OtkazZayavkaView(request, idd):
    nzayav = zayavka.objects.filter(status='Новая заявка').order_by('-date_sozd')
    nzayav_count = zayavka.objects.filter(status='Новая заявка').count()
    wzayav = zayavka.objects.filter(status='В работе').order_by('-date_sozd')
    wzayav_count = zayavka.objects.filter(status='В работе').count()
    szayav = zayavka.objects.filter(status='Сделка').order_by('-date_sozd')
    szayav_count = zayavka.objects.filter(status='Сделка').count()
    ozayav = zayavka.objects.filter(status='Отказ').order_by('-date_sozd')
    ozayav_count = zayavka.objects.filter(status='Отказ').count()

    zayav = get_object_or_404(zayavka, pk=idd)
    zayav.status = 'Отказ'
    zayav.date_zakr = datetime.now()
    zayav.save()
    return render(request,'zayavka/all.html',{'tnzayav':nzayav,'tnzayav_count':nzayav_count,
                                              'twzayav':wzayav,'twzayav_count':wzayav_count,'tszayav':szayav,
                                              'tszayav_count':szayav_count,'tozayav':ozayav,'tozayav_count':ozayav_count,})