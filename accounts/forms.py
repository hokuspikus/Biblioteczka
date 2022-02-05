from django import forms
from django.core.exceptions import ValidationError


def pass_length_validation(value):
    if len(value) < 8:
        raise ValidationError('Password is too short')

class LoginForm(forms.Form):
    username = forms.CharField(label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Hasło'}))


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Hasło'}))

