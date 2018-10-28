import datetime

from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from zastroishik.forms import loginform
from zayavka.forms import zayavkaFromSaitForm


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
            post.date_sozd = datetime.datetime.now()
            post.kanal_pr = 'Заявка с сайта'
            post.status = 'Новая заявка'
            ss = 'От ' + post.name_kl +' тел.'+str(post.tel)
            send_mail('Поступила новая заявка на сайт', ss , 'zhem-otchet@mail.ru',
                      ['hamster197@mail.ru'], fail_silently=False, html_message=ss)
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
            post.date_sozd = datetime.datetime.now()
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
    return render(request,'main/ipoteca.html')

def FZ214PageView(request):
    return render(request,'main/fz214.html')

def RasrochkaPageView(request):
    return render(request,'main/rasr.html')

def RemontPageView(request):
    return render(request,'main/remon.html')

def PoliticaConfPageView(request):
    return render(request,'main/Politicakonf.html')

