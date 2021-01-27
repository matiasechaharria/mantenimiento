from django.contrib import admin

# Register your models here.
from .models import Proveedor, Rubro

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['empresa','telefono','direccion','website','horario','comentario','activo','rubro']
    pass

class RubroAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    pass

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Rubro, RubroAdmin)
