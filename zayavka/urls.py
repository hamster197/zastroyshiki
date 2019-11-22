"""zastroishik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name='zayavka'
urlpatterns = [
    path(r'new/', views.newZayavView, name='newZayav'),
    path(r'all/', views.allZayavkaView, name='allZayav'),
    path(r'inwork/<int:idd>/', views.inWorkZayavkaView, name='flatsInWork'),
    path(r'sdelka/<int:idd>/', views.SdelkaZayavkaView, name='flatsSdelka'),
    path(r'otkaz/<int:idd>/', views.OtkazZayavkaView, name='flatsOtkaz'),
]
