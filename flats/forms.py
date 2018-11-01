from django import forms

from flats.models import flat


class FlatChangeForm(forms.ModelForm):
    class Meta:
        model = flat
        fields = ('cena_za_metr','status','canal_prodagi')