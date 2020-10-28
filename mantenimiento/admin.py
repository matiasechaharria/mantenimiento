from django.contrib import admin

# Register your models here.
from .models import Equipo, TipoEquipo, Marca, Modelo, EstadoTecnico
from .models import Instituto, Departamento, Servicio, Sector, Contacto

class EquipoAdmin(admin.ModelAdmin):
    list_filter = ['tipoEquipo', 'servicio','nombre','activo']
    list_display = ['id','nombre','tipoEquipo','marca','servicio','numero_de_serie']

    pass
class TipoEquipoAdmin(admin.ModelAdmin):
    pass
class MarcaAdmin(admin.ModelAdmin):
    pass
class ModeloAdmin(admin.ModelAdmin):
    pass
class EstadoTecnicoAdmin(admin.ModelAdmin):
    pass
class InstitutoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    pass
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre','instituto']
    pass
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'departamento']
    pass
class SectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'servicio']
    pass
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono','email','servicio']
    list_filter = ['nombre','servicio']

    pass
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(TipoEquipo, TipoEquipoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(EstadoTecnico, EstadoTecnicoAdmin)
admin.site.register(Instituto, InstitutoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Contacto, ContactoAdmin)