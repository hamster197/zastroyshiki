from django.shortcuts import render


def FlatPageView(request):
    return render(request,'flats/main.html')