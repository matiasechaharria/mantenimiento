from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.



class EstadoTecnico(models.Model):
    """
     EstadoTecnico
    """
    nombre = models.CharField( max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)



class Marca (models.Model):
    """
        Marca
    """
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)

class Modelo (models.Model):
    """
        Modelo
    """

    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    def __str__(self):
       return str(self.nombre)

class TipoEquipo(models.Model):
    """
        tipos de equipo
    """
    nombre = models.CharField(verbose_name='Tipo de Equipo', max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)

class Equipo (models.Model):
    """
        Equipo de laboratorio
    """
    servicio= models.ForeignKey('Servicio', on_delete=models.CASCADE)
    tipoEquipo = models.ForeignKey('TipoEquipo', on_delete=models.CASCADE)
    img= models.ImageField(null=True, default=None, upload_to = "imagenes")
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    #sector= models.ForeignKey('Sector', on_delete=models.CASCADE)
#estado_tecnico = models.ForeignKey('EstadoTecnico', on_delete=models.CASCADE)

    nombre = models.CharField(verbose_name='nombre', max_length=30)
    numero_de_serie = models.CharField(verbose_name='numero de serie', max_length=30, unique=True)

    activo = models.BooleanField(default=True)
    dateTimeAlta = models.DateTimeField()
    #dateTimeBaja = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)



##---------------------------------------------------------------------------------------#
## cosas del cliente

class Instituto (models.Model):
    """
        Instituto
    """
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)

class Departamento (models.Model):
    """
        Departamento
    """
    instituto = models.ForeignKey('Instituto',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
       return str(self.nombre)

class Servicio (models.Model):
    """
        servicio
    """

    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
       return str(self.nombre)

class Sector (models.Model):
    """
        Sector
    """

    servicio = models.ForeignKey('servicio', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)

    def __str__(self):
       return str(self.nombre)



class Contacto(models.Model):
    """
        personas de contacto para los servicios
    """
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    telefono = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length = 100,unique=True)
    comentario = models.CharField(max_length=30, unique=True)


    def __str__(self):
        return str(self.nombre)






class FormAddUser(UserCreationForm):
    class meta:
        model = User
        fields = ('__all__',)
