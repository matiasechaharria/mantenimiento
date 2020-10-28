from django.db import models
from mantenimiento.models import Equipo
# Create your models here.


class Preventivo(models.Model):
    #dateTime = models.DateTimeField() #fecha en la que se escribe ne la base
    preventivo = models.CharField(max_length=500)
    fecha = models.DateField() #fecha en la que se hiso el informe
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    #persona = models.ForeignKey('persona', on_delete=models.CASCADE)


    #def __str__(self):
     #  return str(self.nombre)