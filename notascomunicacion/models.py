from django.db import models
#from mantenimiento.models import Servicio

# Create your models here.
class NotaComunicacion(models.Model):
    asunto = models.CharField(max_length=200)
    resumen = models.CharField(max_length=500)
    #archivo = models.FileField(upload_to='notascomunicacion_file/')

    #servicio = models.ForeingKey(Servicio,on_delete=models.CASCADE)
