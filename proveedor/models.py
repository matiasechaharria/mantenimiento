from django.db import models

# Create your models here.

class Proveedor(models.Model):
    """Tabla de proveedor"""
    empresa = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(verbose_name="teléfono",max_length=50,null=True, default=None, unique=True, blank=True)
    interno = models.CharField(max_length=50,null=True, default=None, unique=True, blank=True)
    direccion= models.CharField(verbose_name="dirección",max_length=50,null=True, default=None, blank=True)
    website = models.CharField(max_length=50,null=True, default=None, blank=True)
    horario = models.CharField(verbose_name="horario de atención",max_length=50,null=True, default=None, blank=True)
    comentario = models.CharField(max_length=50,null=True, default=None, blank=True)
    rubro = models.ForeignKey('Rubro', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.empresa)



class Rubro(models.Model):
    """Tabla de rubros del proveedor"""
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.nombre)
