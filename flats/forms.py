from django import forms
from django.forms import DateInput, CheckboxInput, CheckboxSelectMultiple

from flats.models import flat


class FlatChangeForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ('cena_za_metr','status',)

class FlatBronForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ['fio_pokupatel','tel_pokupatel','bron_date_end','bron_vneseno','agenstvo','prim']
        widgets = {
            'bron_date_end': DateInput(format='%Y-%m-%d', attrs={'type' : 'date'}),
            'agenstvo': CheckboxSelectMultiple(),
        }