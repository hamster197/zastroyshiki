from django import forms
from zayavka.models import zayavka


class zayavkaFromSaitForm(forms.ModelForm):
    class Meta:
        model = zayavka
        fields = ('name_kl','tel',)

class allZayvkaAdd(forms.ModelForm):
    class Meta:
        model = zayavka
        fields =['kanal_pr','name_kl','tel','budget','text']