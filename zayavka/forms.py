from django import forms
from zayavka.models import zayavka


class zayavkaFromSaitForm(forms.ModelForm):
    class Meta:
        model = zayavka
        fields = ('name_kl','tel',)
