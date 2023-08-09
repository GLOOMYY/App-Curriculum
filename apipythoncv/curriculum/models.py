from django.db import models
from users.models import User

# Create your models here.

class Tecnologias(models.Model):
  nombre_tecnologia = models.CharField(verbose_name='Nombre de Tecnologia', max_length=50)
  
  class Meta:
    verbose_name = 'Tecnologia'
    verbose_name_plural = 'Tecnologias'
    
  def __str__(self):
    return self.nombre_tecnologia

class ProyectosDev(models.Model):
  nombre = models.CharField(verbose_name='Nombre de Proyecto',max_length=100)
  link = models.URLField(verbose_name='Link de Proyecto',max_length=100)
  tecnologia = models.ManyToManyField(Tecnologias,verbose_name='Tecnologias utilizadas')
  anio_creacion = models.DateField(verbose_name='Año de Terminacion', blank=True, null=True)
  descripcion = models.TextField(verbose_name='Descripcion de Proyecto')
  id_user = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True, auto_now = False, null=True, blank=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True, null=True, blank=True)
  
  class Meta:
    verbose_name = 'Proyecto Desarrollado'
    verbose_name_plural = 'Proyectos Desarrollados'
    
  def __str__(self):
    return f'{self.nombre} {self.link}'
  
class ExperienciaLb(models.Model):
  experiencia = models.BooleanField(default=False)
  empresa = models.CharField(max_length=100)
  cargo = models.CharField(max_length=100)
  descripcion = models.TextField()
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField(null=True, blank=True)
  id_user = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True, auto_now = False, null=True, blank=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True, null=True, blank=True)
  
  class Meta:
    verbose_name = 'Experiencia Laboral'
    verbose_name_plural = 'Experiencias Laborales'
  
  def __str__(self):
    return f'{self.cargo} {self.empresa}'


class Estudios(models.Model):
  
  ESTUDIOS = [
    ("Primaria","Primaria"),
    ("Secundaria", "Secundaria"),
    ("Curso","Curso"),
    ("Tecnico","Tecnico"),
    ("Tecnologo","Tecnologo"),
    ("Pregrado","Pregrado"),
    ("Posgrado","Posgrado")
  ]
  estudio = models.CharField(verbose_name='Tipo de Estudio',choices=ESTUDIOS, max_length=100, null=True, blank=True)
  titulo = models.CharField(verbose_name='Titulo Obtenido',max_length=100)
  institucion = models.CharField(verbose_name='Institución',max_length=100)
  on_course = models.BooleanField(verbose_name='En Curso', default=False)
  fecha_fin = models.DateField(null=True, blank=True)
  id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True, auto_now = False, null=True, blank=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True, null=True, blank=True)
  
  class Meta:
    verbose_name = 'Estudio'
    verbose_name_plural = 'Estudios'
  
  def __str__(self):
    return f'{self.titulo}'

class Extras(models.Model):
  extra = models.CharField(verbose_name='Extra, Hobbies y demas',max_length=100)
  id_user = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True, auto_now = False, null=True, blank=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True, null=True, blank=True)
  
  class Meta:
    verbose_name = 'Extra'
    verbose_name_plural = 'Extras'
  
  def __str__(self):
    return f'{self.extra}'
  
class Habilidades(models.Model):
  habilidad = models.CharField(verbose_name='Habilidad',max_length=100)
  nivel = models.CharField(verbose_name='Nivel', max_length=100, choices=Nivel)
  id_user = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True, auto_now = False, null=True, blank=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True, null=True, blank=True)
  
  class Meta:
    verbose_name = 'Habilidad'
    verbose_name_plural = 'Habilidades'
  
  def __str__(self):
    return f'{self.habilidad}'
  
class Facts(models.Model):
  pass