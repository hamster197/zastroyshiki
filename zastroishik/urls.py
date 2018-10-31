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
from django.contrib import admin
from django.urls import path, include
import flats
from flats import views
from . import views

app_name='zastr'
urlpatterns = [
    #path(r'jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path(r'select2/', include('django_select2.urls')),
    path(r'login', views.loginView, name='login'),
    path(r'logout', views.logoutView, name='logout'),
    path(r'', views.mainPageView, name='mainpage'),
    path(r'about', views.AboutPageView, name='aboutpage'),
    path(r'apparts', flats.views.FlatPageView, name='allFlatsIndex'),
    path(r'hodstroitelstva', views.HodStroitPageView, name='hodStroy'),
    path(r'documents', views.DokumentsPageView, name='doki'),
    path(r'contacts', views.ContactsPageView, name='contack'),
    path(r'ipoteca', views.IpotecaPageView, name='ipoteca'),
    path(r'fz214', views.FZ214PageView, name='fz214'),
    path(r'rasr', views.RasrochkaPageView, name='rasr'),
    path(r'remont', views.RemontPageView, name='remont'),
    path(r'politica', views.PoliticaConfPageView, name='politica'),

]
