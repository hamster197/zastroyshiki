from django import forms

class loginform(forms.Form):
    username=forms.CharField(max_length=20, label='Имя пользователя')
    passw=forms.CharField(max_length=10,widget=forms.PasswordInput, label='Пароль')