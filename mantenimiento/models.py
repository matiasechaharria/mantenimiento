from django.db import models

# Create your models here.


class Equipo (models.Model):
    """
        Equipo de laboratorio
    """
    nombre = models.CharField(verbose_name='nombre', max_length=30)
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    tipoEquipo = models.ForeignKey('TipoEquipo', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    numero_de_serie = models.CharField(verbose_name='numero de serie', max_length=30, unique=True)

    activo = models.BooleanField(default=True)
    dateTimeAlta = models.DateTimeField()
    dateTimeBaja = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class EstadoTecnico(models.Model):
    """
     Model
    """
    nombre = models.CharField(verbose_name='EstadoTecnico', max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)

class Modelo(models.Model):
    """
     Model
    """
    nombre = models.CharField(verbose_name='modelo', max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)

class Marca(models.Model):
    """
    Marca
    """
    nombre = models.CharField(verbose_name='Marca', max_length=30, unique=True)

    def __str__(self):
        return str(self.nombre)

class TipoEquipo(models.Model):
    """
    tipos de equipo
    """
    nombre = models.CharField(verbose_name='Tipo de Equipo', max_length=30, unique=True)

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
    nombre = models.CharField(max_length=30, unique=True)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    def __str__(self):
       return str(self.nombre)


class Contacto(models.Model):
    """
        personas de contacto para los servicios
    """
    nombre = models.CharField(max_length=30, unique=True)
    telefono = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length = 100,unique=True)
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)


class Sector (models.Model):
    """
        Sector
    """
    nombre = models.CharField(max_length=30, unique=True)
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    def __str__(self):
       return str(self.nombre)