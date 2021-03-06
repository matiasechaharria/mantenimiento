from django.db import models
#from mantenimiento.models import Servicio
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage, FileSystemStorage
# Create your models here.
from mantenimiento.models import Servicio

fs = FileSystemStorage(location="/notascomunicacion_file/")

class NotaComunicacion(models.Model):
    #servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)

    asunto = models.CharField(max_length=200)
    resumen = models.CharField(max_length=500)
    #archivo = models.ImageField(upload_to='notascomunicacion_file/')
    file= models.FileField(null=True,blank=True, default=None, upload_to='notascomunicacion_file/%Y/%m/%d')

    def __str__(self):
        return str(self.asunto)


    #servicio = models.ForeingKey(Servicio,on_delete=models.CASCADE)
