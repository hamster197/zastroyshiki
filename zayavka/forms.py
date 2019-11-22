from django import forms
from zayavka.models import zayavka


class zayavkaFromSaitForm(forms.ModelForm):
    class Meta:
        model = zayavka
        fields = ('name_kl','tel',)
        widgets = {'name_kl': forms.TextInput(attrs={'placeholder': 'Ваше имя*'}),
                   'tel': forms.TextInput(attrs={'placeholder': 'Номер телефона*'})}
        #widgets = {'tel': forms.TextInput(attrs={'placeholder': 'Номер телефона*'})}

class allZayvkaAdd(forms.ModelForm):
    class Meta:
        model = zayavka
        fields =['kanal_pr','name_kl','tel','budget','text']