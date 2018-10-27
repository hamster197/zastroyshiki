from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect

from zastroishik.forms import loginform

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
    return render(request,'main/index.html')

def AboutPageView(request):
    return render(request,'main/about.html')

def HodStroitPageView(request):
    return render(request,'main/hodstroy.html')

def DokumentsPageView(request):
    return render(request,'main/doki.html')

def ContactsPageView(request):
    return render(request,'main/contacts.html')

def IpotecaPageView(request):
    return render(request,'main/ipoteca.html')

def FZ214PageView(request):
    return render(request,'main/fz214.html')

def RasrochkaPageView(request):
    return render(request,'main/rasr.html')

def RemontPageView(request):
    return render(request,'main/remon.html')

