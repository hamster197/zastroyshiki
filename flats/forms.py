from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, CheckboxSelectMultiple, TextInput
from phonenumber_field.formfields import PhoneNumberField

from flats.models import flat, agenstv_spr
from zayavka.models import zayavka


# class FlatChangeForm(forms.ModelForm):
#     class Meta:
#         model = flat
#         fields = ('cena_za_metr','status',)
class FlatChangeForm(forms.Form):
    cena_za_metr = forms.IntegerField(label='Цена')
    cena_za_metr = forms.FloatField(label='Цена')
    st_ch = (('Свободна','Свободна'),('Бронь','Бронь'),('Продана','Продана'))
    status = forms.ChoiceField(label='Статус', choices=st_ch)

class FlatBronForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ['fio_pokupatel','tel_pokupatel','kanal_pr','bron_date_end','bron_vneseno','agenstvo','prim']
        widgets = {
            'bron_date_end': DateInput(format='%Y-%m-%d', attrs={'type' : 'date'}),
            'agenstvo': CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super(FlatBronForm, self).clean()
        if int(cleaned_data['bron_vneseno'])<10000:
                raise ValidationError('Внесенно брони меньше 10000!', code='invalid')

class FlatSdelkaForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ['fio_pokupatel','tel_pokupatel','kanal_pr','agenstvo','prim']
        widgets = {
            'agenstvo': CheckboxSelectMultiple(),
        }

class FlatZayvkaForm(forms.ModelForm):
    class Meta:
        model = zayavka
        fields =['tel',]

class EstateAddForm(forms.ModelForm):
    class Meta:
        model = agenstv_spr
        fields = ['ag_name',]

