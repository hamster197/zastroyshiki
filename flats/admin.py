from django.contrib import admin

from flats.models import flat, Planirovki

class flatFields(admin.ModelAdmin):
    list_display = ('kv_numb','korpus','etag','komnat','metrag','status')
    list_filter = ('korpus','etag',)

class planirovkaFelds(admin.ModelAdmin):
    list_display = ('corp_name','pl_name')
    list_filter = ('corp_name',)

admin.site.register(flat, flatFields)
admin.site.register(Planirovki, planirovkaFelds)
