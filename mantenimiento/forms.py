from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Contacto

class LogInForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
