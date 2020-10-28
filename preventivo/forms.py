from django import forms

from .models import Preventivo

class PreventivoForm(forms.ModelForm):

    class Meta:
        model = Preventivo
        fields = ('preventivo', 'fecha','equipo',)
