from django.contrib import admin
from .models import Preventivo
# Register your models here.


class PreventivoAdmin(admin.ModelAdmin):
    list_display = ['preventivo', 'fecha']
    #list_filter = ['equipo','tipoEquipo', 'servicio']
    pass

admin.site.register(Preventivo, PreventivoAdmin)