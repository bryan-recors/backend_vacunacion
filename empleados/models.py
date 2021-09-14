from django.db import models
from django.contrib.auth.models import AbstractUser
#para autocompletar username
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class Usuario(AbstractUser):
    cedula = models.CharField('cedula', max_length=100)
    nombres = models.CharField('Nombres',max_length=100)
    apellidos = models.CharField('Apellidos',max_length=100)
    email = models.EmailField('correo', unique=True)
    username = models.CharField('nombre de usuario', max_length=150, blank=True, null=True, unique=True)
    password = models.CharField('password', max_length=150, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField('Direccion',max_length=500, blank=True, null=True)
    telefono_movil = models.CharField('Celular',max_length=10,blank=True, null=True)
    estado_vacunacion = models.BooleanField('Estado de vacunacion', default=False)
    tipo_vacuna = models.CharField('tipo de vacuna', max_length=100,blank=True, null=True)
    fecha_vacunacion = models.DateField(blank=True, null=True)
    numero_dosis = models.CharField('numero dosis', max_length=100,blank=True, null=True)
    REQUIRED_FIELDS = ['cedula','nombres','apellidos','email']

def set_username(sender, instance, *args, **kwargs):  #callback
    #autocompletar username
    if instance.nombres and not instance.username:
        username = slugify(instance.nombres+instance.apellidos)
        instance.username = username
    if instance.cedula and not instance.password:
        password = slugify(instance.cedula)
        instance.set_password(password)  # encripta contraseña
#antes de guardar ejecute

pre_save.connect(set_username, sender=Usuario)