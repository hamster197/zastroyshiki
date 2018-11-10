from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput, CheckboxSelectMultiple, TextInput
from phonenumber_field.formfields import PhoneNumberField

from flats.models import flat, agenstv_spr
from zayavka.models import zayavka


class FlatChangeForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ('cena_za_metr','status',)

class FlatBronForm(forms.ModelForm):
    fio_pokupatel = forms.CharField(label='dasd',help_text='wqeqweq')
    class Meta:
        model = flat
        fields = ['fio_pokupatel','tel_pokupatel','bron_date_end','bron_vneseno','agenstvo','prim']
        widgets = {
            'bron_date_end': DateInput(format='%Y-%m-%d', attrs={'type' : 'date'}),
            'agenstvo': CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super(FlatBronForm, self).clean()
        if int(cleaned_data['bron_vneseno'])<10000:
                raise ValidationError('Внесенно брони меньше 10000!', code='invalid')


class FlatZayvkaForm(forms.ModelForm):
    tel = PhoneNumberField(help_text='qweqwe')
    class Meta:
        model = zayavka
        fields =['tel',]

class EstateAddForm(forms.ModelForm):
    class Meta:
        model = agenstv_spr
        fields = ['ag_name',]