from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput


class loginform(forms.Form):
    username=forms.CharField(max_length=20, label='Имя пользователя')
    passw=forms.CharField(max_length=10,widget=forms.PasswordInput, label='Пароль')

class SdelkiDateForm(forms.Form):
    date_st =  forms.DateField(label='Начало периода:', widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    date_end = forms.DateField(label='Конец периода:', widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super(SdelkiDateForm, self).clean()
        if cleaned_data['date_st']<cleaned_data['date_end']:
                raise ValidationError('Дата старта меньше даты окончания периода!', code='invalid')



