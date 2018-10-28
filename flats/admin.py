from django.contrib import admin
from flats.models import flat, Planirovki
from zayavka.models import zayavka

class flatFields(admin.ModelAdmin):
    list_display = ('kv_numb','korpus','etag','komnat','metrag','status')
    list_filter = ('korpus','etag',)

class planirovkaFelds(admin.ModelAdmin):
    list_display = ('corp_name','pl_name')
    list_filter = ('corp_name',)

class zayavkaFields(admin.ModelAdmin):
    list_display = ('date_sozd','status','kanal_pr','tel','name_kl')
    list_filter = ('status',)

admin.site.register(flat, flatFields)
admin.site.register(Planirovki, planirovkaFelds)
admin.site.register(zayavka, zayavkaFields)

