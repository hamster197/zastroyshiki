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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
import flats
import blog

app_name='zastr'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'flats/', include('flats.urls')),
    path(r'zayavka/', include('zayavka.urls')),
    path(r'spr/', include('blog.urls')),
    path(r'login', views.loginView, name='login'),
    path(r'logout', views.logoutView, name='logout'),
    path(r'', views.mainPageView, name='mainpage'),
    path(r'about', views.AboutPageView, name='aboutpage'),
    path(r'apparts', flats.views.FlatPageView, name='allFlatsIndex'),
    path(r'hodstroitelstva', views.HodStroitPageView, name='hodStroy'),
    #path(r'hodstroitelstva', blog.views IndexHodStView, name='hodStroy'),
    path(r'documents', views.DokumentsPageView, name='doki'),
    path(r'contacts', views.ContactsPageView, name='contack'),
    path(r'ipoteca', views.IpotecaPageView, name='ipoteca'),
    path(r'fz214', views.FZ214PageView, name='fz214'),
    path(r'rasr', views.RasrochkaPageView, name='rasr'),
    path(r'remont', views.RemontPageView, name='remont'),
    path(r'politica', views.PoliticaConfPageView, name='politica'),
    path(r'analitic', views.AnaliticaView, name='analitics'),
    path(r'sdelki', views.SdekaAnView, name='sdelkistat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
