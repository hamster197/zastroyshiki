from datetime import datetime

from django.shortcuts import render, redirect

# Create your views here.
from zayavka.forms import allZayvkaAdd
from zayavka.models import zayavka


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