from django import forms


class LogInForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)
