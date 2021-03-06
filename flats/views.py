from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from flats.forms import FlatChangeForm, FlatBronForm, FlatZayvkaForm, EstateAddForm, FlatSdelkaForm
from flats.models import flat

#################################
## kvartiri all view
#################################
def FlatPageView(request):
    ###########################
    ## 1 Korpus
    ###########################
    korp1_1etag=flat.objects.filter(korpus='1 корпус',etag='1 Этаж').order_by('id','kv_numb')
    korp1_2etag=flat.objects.filter(korpus='1 корпус',etag='2 Этаж').order_by('id','kv_numb')
    korp1_3etag=flat.objects.filter(korpus='1 корпус',etag='3 Этаж').order_by('id','kv_numb')
    korp1_4etag=flat.objects.filter(korpus='1 корпус',etag='4 Этаж').order_by('id','kv_numb')
    korp1_5etag=flat.objects.filter(korpus='1 корпус',etag='5 Этаж').order_by('id','kv_numb')
    korp1_6etag=flat.objects.filter(korpus='1 корпус',etag='6 Этаж').order_by('id','kv_numb')
    korp1_7etag=flat.objects.filter(korpus='1 корпус',etag='7 Этаж').order_by('kv_numb','id')
    korp1_8etag=flat.objects.filter(korpus='1 корпус',etag='8 Этаж').order_by('id','kv_numb')
    korp1_9etag=flat.objects.filter(korpus='1 корпус',etag='9 Этаж').order_by('id','kv_numb')
    korp1_10etag=flat.objects.filter(korpus='1 корпус',etag='10 Этаж').order_by('id','kv_numb')
    korp1_11etag=flat.objects.filter(korpus='1 корпус',etag='11 Этаж').order_by('id','kv_numb')
    korp1_12etag=flat.objects.filter(korpus='1 корпус',etag='12 Этаж').order_by('id','kv_numb')
    ###########################
    ## 2 Korpus
    ###########################
    korp2_1etag=flat.objects.filter(korpus='2 корпус',etag='1 Этаж').order_by('id','kv_numb')
    korp2_2etag=flat.objects.filter(korpus='2 корпус',etag='2 Этаж').order_by('kv_numb','id')
    korp2_3etag=flat.objects.filter(korpus='2 корпус',etag='3 Этаж').order_by('id','kv_numb')
    korp2_4etag=flat.objects.filter(korpus='2 корпус',etag='4 Этаж').order_by('id','kv_numb')
    korp2_5etag=flat.objects.filter(korpus='2 корпус',etag='5 Этаж').order_by('id','kv_numb')
    korp2_6etag=flat.objects.filter(korpus='2 корпус',etag='6 Этаж').order_by('id','kv_numb')
    korp2_7etag=flat.objects.filter(korpus='2 корпус',etag='7 Этаж').order_by('id','kv_numb')
    korp2_8etag=flat.objects.filter(korpus='2 корпус',etag='8 Этаж').order_by('id','kv_numb')
    korp2_9etag=flat.objects.filter(korpus='2 корпус',etag='9 Этаж').order_by('id','kv_numb')
    korp2_10etag=flat.objects.filter(korpus='2 корпус',etag='10 Этаж').order_by('id','kv_numb')
    korp2_11etag=flat.objects.filter(korpus='2 корпус',etag='11 Этаж').order_by('id','kv_numb')
    korp2_12etag=flat.objects.filter(korpus='2 корпус',etag='12 Этаж').order_by('id','kv_numb')
    ###########################
    ## 2 Korpus
    ###########################
    return render(request,'flats/main.html', {'tkorp1_1etag':korp1_1etag,'tkorp1_2etag':korp1_2etag,
                                              'tkorp1_3etag':korp1_3etag, 'tkorp1_4etag':korp1_4etag,
                                              'tkorp1_5etag': korp1_5etag, 'tkorp1_6etag': korp1_6etag,
                                              'tkorp1_7etag': korp1_7etag, 'tkorp1_7etag': korp1_7etag,
                                              'tkorp1_8etag': korp1_8etag, 'tkorp1_9etag': korp1_9etag,
                                              'tkorp1_10etag': korp1_10etag, 'tkorp1_11etag': korp1_11etag,
                                              'tkorp1_12etag': korp1_12etag,
                                              'tkorp2_1etag': korp2_1etag, 'tkorp2_2etag': korp2_2etag,
                                              'tkorp2_3etag': korp2_3etag, 'tkorp2_4etag': korp2_4etag,
                                              'tkorp2_5etag': korp2_5etag, 'tkorp2_6etag': korp2_6etag,
                                              'tkorp2_7etag': korp2_7etag, 'tkorp2_7etag': korp2_7etag,
                                              'tkorp2_8etag': korp2_8etag, 'tkorp2_9etag': korp2_9etag,
                                              'tkorp2_10etag': korp2_10etag, 'tkorp2_11etag': korp2_11etag,
                                              'tkorp2_12etag': korp2_12etag,
                                              })

# #################################
# ## kvartiri Chang view
# #################################
# @login_required
# def FlatChangeView(request, idd):
#     flats = get_object_or_404(flat, pk=idd)
#     if request.POST:
#         form = FlatChangeForm(request.POST,instance=flats)
#         if form.is_valid():
#                 form.save()
#                 return redirect('allFlatsIndex')
#     form = FlatChangeForm(instance=flats)
#     return render(request,'flats/flatchange.html',{'tform':form})

@login_required
def FlatChangeView(request, idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        form = FlatChangeForm(request.POST)
        if form.is_valid():
            cena = form.cleaned_data['cena_za_metr']
            status = form.cleaned_data['status']
            flats.status = status
            flats.cena_za_metr = cena / flats.planirovka.ploshad
            flats.save()
            return redirect('allFlatsIndex')
    form = FlatChangeForm(initial={'cena_za_metr': flats.cena_za_metr * flats.planirovka.ploshad, 'status': flats.status})
    return render(request,'flats/flatchange.html',{'tform':form})

#################################
## kvartiri bron view
#################################
@login_required
def FlatBronView(request,idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        if 'bron' in request.POST:
            form = FlatBronForm(request.POST, instance=flats)
            if form.is_valid():
                fl = form.save(commit=False)
                fl.bron_date_start = datetime.now()
                fl.status = 'Бронь'
                fl.save()
                form.save_m2m()
                return redirect('allFlatsIndex')
        if 'estateadd' in request.POST:
            form = EstateAddForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('flats:flatsBron', idd=flats.pk)
    form = FlatBronForm(instance=flats)
    estform = EstateAddForm()
    return render(request,'flats/flatbron.html',{'tform':form, 'tEstForm': estform, 'tflat':flats})

#################################
## kvartiri sdelka view
#################################
@login_required
def FlatSdelkaView(request, idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        if 'bron' in request.POST:
            form = FlatSdelkaForm(request.POST, instance=flats)
            if form.is_valid():
                fl = form.save(commit=False)
                fl.sdelka_date = datetime.now()
                fl.status = 'Продана'
                fl.save()
                form.save_m2m()
                return redirect('allFlatsIndex')
        if 'estateadd' in request.POST:
            form = EstateAddForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('flats:flatsSdelka', idd=flats.pk)
    form = FlatSdelkaForm(instance=flats)
    estform = EstateAddForm()
    return render(request,'flats/flatsdelka.html',{'tform':form, 'tEstForm': estform, 'tflat':flats})

#################################
## kvartiri zakazat bron view
#################################
def FlatZayavkaPostView(request, idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        form = FlatZayvkaForm(request.POST)
        if form.is_valid():
            zayv = form.save(commit=False)
            zayv.date_sozd = datetime.now()
            zayv.kanal_pr = 'Заявка с сайта(Бронь)'
            zayv.corpus = flats.korpus
            zayv.comnat = flats.planirovka.komnat
            zayv.ploshad = str(flats.planirovka.ploshad)
            zayv.kv_numb = flats.kv_numb
            zayv.stoimost = flats.planirovka.ploshad * flats.cena_za_metr
            zayv.status = 'Новая заявка'
            ss = 'Поступила новая заявка на сайт(Бронь) тел. клиента ' + str(zayv.tel)+', ' + flats.korpus +', '+flats.planirovka.komnat+',№ кв. '+flats.kv_numb
            send_mail('Поступила новая заявка на сайт(Бронь)', ss , 'zhem-otchet@mail.ru',
                      ['newhousesochi1@mail.ru'], fail_silently=False, html_message=ss)
            zayv.save()
            return redirect('allFlatsIndex')
        raise print(form.errors)
    zayav = FlatZayvkaForm()
    return render(request,'flats/flatZayav.html',{'tform':zayav, 'tflat':flats})
