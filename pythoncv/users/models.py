from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  email = models.EmailField('Correo Electrónico', unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
  photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='usuarios/')
  
  profile_profesional = models.TextField(verbose_name='Perfil Profesional', null=True, blank=True)
  resume_profesional = models.TextField(verbose_name='Resumen Profesional', null=True, blank=True)
  resume_skills = models.TextField(verbose_name='Resumen Habilidades', null=True, blank=True)
  occupation_job = models.CharField(verbose_name='Ocupación', max_length=150)
  linkedin = models.URLField(verbose_name='Linkedin', null=True, blank=True)
  website = models.URLField(verbose_name='Web Site', null=True, blank=True)
  telephone = models.CharField(verbose_name='Telephone',max_length=50, null=True, blank=True)
  
  pais = models.CharField(verbose_name='Pais',max_length=50)
  ciudad = models.CharField(verbose_name='Ciudad',max_length=50)
  birthday = models.DateField(verbose_name='Cumpleaños', null=True, blank=True)
  
  # Validadores
  reclutador = models.BooleanField(verbose_name='Reclutador', default=False)
  experiencia = models.BooleanField(verbose_name='Experiencia', default=False)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True)