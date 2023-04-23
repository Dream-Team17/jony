from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class RegisterForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password_1 = forms.CharField(widget=forms.PasswordInput, min_length=5, label='Пароль')
    password_2 = forms.CharField(widget=forms.PasswordInput, min_length=5, label='Повторите пароль')