from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from flats.forms import FlatChangeForm, FlatBronForm
from flats.models import flat
from zastroishik import urls

#################################
## kvartiri all view
#################################
def FlatPageView(request):
    ###########################
    ## 1 Korpus
    ###########################
    korp1_1etag=flat.objects.filter(korpus='1 корпус',etag='1 Этаж')
    korp1_2etag=flat.objects.filter(korpus='1 корпус',etag='2 Этаж')
    korp1_3etag=flat.objects.filter(korpus='1 корпус',etag='3 Этаж')
    korp1_4etag=flat.objects.filter(korpus='1 корпус',etag='4 Этаж')
    korp1_5etag=flat.objects.filter(korpus='1 корпус',etag='5 Этаж')
    korp1_6etag=flat.objects.filter(korpus='1 корпус',etag='6 Этаж')
    korp1_7etag=flat.objects.filter(korpus='1 корпус',etag='7 Этаж')
    korp1_8etag=flat.objects.filter(korpus='1 корпус',etag='8 Этаж')
    korp1_9etag=flat.objects.filter(korpus='1 корпус',etag='9 Этаж')
    korp1_10etag=flat.objects.filter(korpus='1 корпус',etag='10 Этаж')
    korp1_11etag=flat.objects.filter(korpus='1 корпус',etag='11 Этаж')
    korp1_12etag=flat.objects.filter(korpus='1 корпус',etag='12 Этаж')
    ###########################
    ## 2 Korpus
    ###########################
    korp2_1etag=flat.objects.filter(korpus='2 корпус',etag='1 Этаж')
    korp2_2etag=flat.objects.filter(korpus='2 корпус',etag='2 Этаж')
    korp2_3etag=flat.objects.filter(korpus='2 корпус',etag='3 Этаж')
    korp2_4etag=flat.objects.filter(korpus='2 корпус',etag='4 Этаж')
    korp2_5etag=flat.objects.filter(korpus='2 корпус',etag='5 Этаж')
    korp2_6etag=flat.objects.filter(korpus='2 корпус',etag='6 Этаж')
    korp2_7etag=flat.objects.filter(korpus='2 корпус',etag='7 Этаж')
    korp2_8etag=flat.objects.filter(korpus='2 корпус',etag='8 Этаж')
    korp2_9etag=flat.objects.filter(korpus='2 корпус',etag='9 Этаж')
    korp2_10etag=flat.objects.filter(korpus='2 корпус',etag='10 Этаж')
    korp2_11etag=flat.objects.filter(korpus='2 корпус',etag='11 Этаж')
    korp2_12etag=flat.objects.filter(korpus='2 корпус',etag='12 Этаж')
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

#################################
## kvartiri Chang view
#################################
@login_required
def FlatChangeView(request, idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        form = FlatChangeForm(request.POST,instance=flats)
        if form.is_valid():
                form.save()
                return redirect('allFlatsIndex')
    form = FlatChangeForm(instance=flats)
    return render(request,'flats/flatchange.html',{'tform':form})

#################################
## kvartiri bron view
#################################
@login_required
def FlatBronView(request,idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        form = FlatBronForm(request.POST,instance=flats)
        if form.is_valid():
                form.save()
                return redirect('allFlatsIndex')
    form = FlatBronForm(instance=flats)
    return render(request,'flats/flatbron.html',{'tform':form})

#################################
## kvartiri sdelka view
#################################
@login_required
def FlatSdelkaView(request, idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        form = FlatChangeForm(request.POST,instance=flats)
        if form.is_valid():
                form.save()
                return redirect('allFlatsIndex')
    form = FlatChangeForm(instance=flats)
    komnat = flats.planirovka.komnat
    return render(request,'flats/flatZayav.html',{'tform':form, 'tkomnat':komnat})

#################################
## kvartiri zakazat bron view
#################################
@login_required
def FlatZayavkaPostView(request, idd):
    flats = get_object_or_404(flat, pk=idd)
    if request.POST:
        form = FlatChangeForm(request.POST,instance=flats)
        if form.is_valid():
                form.save()
                return redirect('allFlatsIndex')
    form = FlatChangeForm(instance=flats)
    komnat = flats.planirovka.komnat
    return render(request,'flats/flatZayav.html',{'tform':form, 'tkomnat':komnat})