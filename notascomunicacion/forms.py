from django import forms
from django.forms import ModelForm
from django.db import models
from .models import NotaComunicacion

class NotaComunicacionForm(forms.ModelForm):
    class Meta:
        model = NotaComunicacion
        fields = '__all__'
