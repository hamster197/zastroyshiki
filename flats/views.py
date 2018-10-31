from django.shortcuts import render

from flats.models import flat


def FlatPageView(request):
    return render(request,'flats/main.html')

