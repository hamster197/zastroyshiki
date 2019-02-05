from django import forms

from .models import stavki_ip, blog_hod_st


class StavkiEditForm(forms.ModelForm):
    class Meta:
        model = stavki_ip
        fields =['sber_proc','sber_vznos','sber_srok',
                 'vtb_proc','vtb_vznos','vtb_srok',
                 'alfa_proc','alfa_vznos','alfa_srok',
                 'gaz_proc','gaz_vznos','gaz_srok',
                 'prom_proc','prom_vznos','prom_srok',
                 'sel_proc','sel_vznos','sel_srok',]


class NewPostHodStrForm(forms.ModelForm):
    class Meta:
        model = blog_hod_st
        fields = ['date_sozd','nazv','text', 'pict1', 'pict2', 'pict3', 'pict4']
        widgets = {
            'date_sozd': forms.TextInput(attrs={'type': 'date'}),
        }
