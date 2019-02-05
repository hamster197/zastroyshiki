from django.contrib import admin
from flats.models import flat, Planirovki, agenstv_spr
from zayavka.models import zayavka
from blog.models import stavki_ip, blog_hod_st


class flatFields(admin.ModelAdmin):
    list_display = ('kv_numb','korpus','etag','cena_za_metr','status',)
    list_filter = ('korpus','etag',)

class planirovkaFelds(admin.ModelAdmin):
    list_display = ('pl_name','komnat', 'ploshad', 'pict')
    list_filter = ('komnat',)
    ordering = ('pl_name',)

class zayavkaFields(admin.ModelAdmin):
    list_display = ('date_sozd','status','kanal_pr','tel','name_kl')
    list_filter = ('status',)

class ag_sprFields(admin.ModelAdmin):
    list_display = ['ag_name','kol_sdel']

class stavka_fields(admin.ModelAdmin):
    list_display = ['']

class hotStFields(admin.ModelAdmin):
    list_display = ['date_sozd','nazv']

admin.site.register(flat, flatFields)
admin.site.register(Planirovki, planirovkaFelds)
admin.site.register(agenstv_spr, ag_sprFields)
admin.site.register(zayavka, zayavkaFields)
admin.site.register(stavki_ip)
admin.site.register(blog_hod_st, hotStFields )

