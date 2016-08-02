from django.db import models
from django.utils import timezone

# Create your models here.

#tabla de Equipo
class Equipo(models.Model):
    nombreIdentificativo = models.CharField(max_length=10,blank=True,null=True)
    nombreEquipo = models.CharField(max_length=20)
    telefono =models.CharField(max_length=10,blank=True,null=True)
    #torneo = models.ForeignKey('Torneo')

    def __str__(self):
        return self.nombreEquipo

#tabla de Persona
class Persona(models.Model):
    apellido = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    dni = models.IntegerField()
    SEXO_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    )
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICES)

    def __str__(self):
        return self.nombres +' '+self.apellido

#tabla de Jugador
class Jugador(Persona):
    equipo = models.ForeignKey('Equipo')
    ESPECIALIDAD_CHOICES = (
        ('CO', 'COLOCADOR'),
        ('LI', 'LIBERO'),
        ('CE', 'CENTRAL'),
        ('AT', 'ATAQUE'),
        ('OP', 'OPUESTO'),
    )
    especialidad = models.CharField(max_length=2,choices=ESPECIALIDAD_CHOICES,null=True)

#tabla de Arbitro
class Arbitro(Persona):
    equipo = models.ForeignKey('Equipo')
    ESPECIALIDAD_CHOICES = (
        ('A1', 'PRIMER ARBITRO'),
        ('A2', 'SEGUNDO ARBITRO'),
        ('AN', 'ANOTADOR'),
        ('AS', 'ASISTENTE'),
        ('JU', 'JUEZ DE LINEA'),
    )
    especialidad = models.CharField(max_length=2,choices=ESPECIALIDAD_CHOICES,null=True)

#tabla de Torneo

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20,blank=True,null=True)
    localidad = models.CharField(max_length=20, blank=True,null=True)
    direccion = models.CharField(max_length=30, blank=True,null=True)
    fechaRegistro = models.DateField(default=timezone.now)
    fechaInicio = models.DateField(blank=True,null=True)
    equipos = models.ManyToManyField(Equipo)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Fecha(models.Model):
    nombreFecha = models.CharField(max_length=10)
    datosJornada = models.CharField(max_length=20,blank=True,null=True)
    torneo = models.ForeignKey('Torneo')

    def __str__(self):
        return self.nombreFecha

class Partido(models.Model):
    fechaPartido = models.DateField(blank=True,null=True)
    horaPartido = models.TimeField(blank=True,null=True)
    datosPartido = models.CharField(max_length=40,blank=True,null=True)
    fecha = models.ForeignKey('Fecha')
    #local = models.OneToOneField('Equipo',related_name='partido_local_equipo')
    local = models.ForeignKey('Equipo',related_name='partido_local_equipo')
    visitante = models.ForeignKey('Equipo',related_name='partido_visitante_equipo')
    #visitante = models.OneToOneField('Equipo',related_name='partido_visitante_equipo')
    golLocal = models.IntegerField(blank=True,null=True)
    golVisitante = models.IntegerField(blank=True,null=True)
    cargado = models.BooleanField(default=False)

    def __str__(self):
        return self.fecha.nombreFecha+' vs '

class Posicion(models.Model):
    idTorneo = models.IntegerField()
    equipo = models.ForeignKey('Equipo')
    pj = models.IntegerField(blank=True)
    pg = models.IntegerField(blank=True)
    ppa1 = models.IntegerField(blank=True)
    ppa0 = models.IntegerField(blank=True)
    gf = models.IntegerField(blank=True)
    gc = models.IntegerField(blank=True)
    coefSet = models.FloatField(blank=True)
    puntos= models.IntegerField(blank=True)

    def __str__(self):
        return self.idTorneo+' - '+self.equipo.nombreEquipo




