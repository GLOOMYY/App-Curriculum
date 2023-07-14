from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  email = models.EmailField('Correo Electrónico', unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='media/img/usuarios/')
  resumen = models.TextField(verbose_name='Resumen', blank=True, null=True)
  pais = models.CharField(verbose_name='Pais',max_length=50)
  ciudad = models.CharField(verbose_name='Ciudad',max_length=50)
  reclutador = models.BooleanField(verbose_name='Reclutador', default=False)
  experiencia = models.BooleanField(verbose_name='Experiencia', default=False)
  created = models.DateTimeField(verbose_name='Creado el',auto_now_add=True, auto_now = False, null=True, blank=True)
  modified = models.DateTimeField(verbose_name='Modificado el',auto_now=True, null=True, blank=True)