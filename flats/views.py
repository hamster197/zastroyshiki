from django.shortcuts import render

from flats.forms import FlatChangeForm
from flats.models import flat


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
    return render(request,'flats/main.html', {'tkorp1_1etag':korp1_1etag,'tkorp1_2etag':korp1_2etag,
                                              'tkorp1_3etag':korp1_3etag, 'tkorp1_4etag':korp1_4etag,
                                              'tkorp1_5etag': korp1_5etag, 'tkorp1_6etag': korp1_6etag,
                                              'tkorp1_7etag': korp1_7etag, 'tkorp1_7etag': korp1_7etag,
                                              'tkorp1_8etag': korp1_8etag, 'tkorp1_9etag': korp1_9etag,
                                              'tkorp1_10etag': korp1_10etag, 'tkorp1_11etag': korp1_11etag,
                                              'tkorp1_12etag': korp1_12etag, })

def FlatChangeView(request, idd):
    form = FlatChangeForm()
    return render(request,'flats/flatchange.html',{'tform':form})