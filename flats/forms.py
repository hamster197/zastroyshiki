from django import forms
from django.forms import DateField, Textarea, DateInput

from flats.models import flat


class FlatChangeForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ('cena_za_metr','bron_date_end','status','canal_prodagi')
        widgets = {
            'bron_date_end': DateInput(format='%Y-%m-%d', attrs={'type' : 'date'}),
        }