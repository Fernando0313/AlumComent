from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .authManager import ManejoUsuarios
# Create your models here.


class UsuarioModel(AbstractBaseUser,PermissionsMixin):

   
    
    # si queremos modificar todo el auth model entonces tendremos que usar el AbstractBaseUser, si quieremos solamente modificar first_name, last_name, entonces usaremos el AbstractUser
    # PermissionsMixin => es la clase encargada de dar todos los permisos a nivel administrativo
    TIPO_USUARIO = [(1, 'ADMINISTRADOR'), (2, 'anonimo'), (3, 'idat')]

    usuarioId = models.AutoField(
        primary_key=True, db_column='id', unique=True, null=False)

    usuarioNombre = models.CharField(max_length=50, db_column='nombre')

    usuarioApellido = models.CharField(
        max_length=50, db_column='apellido', verbose_name='Apellido del usuario')

    usuarioCorreo = models.EmailField(
        max_length=50, db_column='email', unique=True)

    usuarioTipo = models.IntegerField(choices=TIPO_USUARIO, default=2,db_column='tipo')

    password = models.TextField(null=True)

    # configurar los campos base de nuestro modelo auth
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # TODO LO SIGUIENTE ES PARA CUANDO VAYAMOS A INGRESAR UN ADMINISTRADOR POR CONSOLA:

    # ahora agregamos el comportamiento cuando se llame al createsuperuser y al create user
    objects = ManejoUsuarios()

    # definimos la columna que sera la encargada de validar que el usuario sea unico e irrepetible
    USERNAME_FIELD = 'usuarioCorreo'

    # es lo que pedira la consola cuando se llame al createsuperuser
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioApellido', 'usuarioTipo']

    class Meta:
        db_table = 'usuarios'
    


class AlumnosModel(models.Model):
    usuarioId = models.AutoField(
        primary_key=True, null=False, db_column='id', unique=True)

    usuarioNombre = models.CharField(
        max_length=100, db_column='nombre', null=False)

    usuarioApellido = models.CharField(
        max_length=100, db_column='apellido', null=False)
    
    usuarioDni = models.CharField(
        max_length=8, db_column='dni', null=True)
    
    usuarioCodigo = models.CharField(
        max_length=9, db_column='codigo', null=True)
    
    # usuarioFoto = models.ImageField(
    #     upload_to='platos',db_column='foto', null=True)
    usuarioCalificacion = models.CharField(
        max_length=5,db_column='calificacion', null=True
    )

    class Meta:
        db_table = 'alumnos'

class FotoModel(models.Model):
    fotoId = models.AutoField(
        primary_key=True, null=False, db_column='id', unique=True)
    
    fotoUrl = models.CharField(max_length=280,db_column='url', null=False)

    alumno = models.ForeignKey(
        to=AlumnosModel, related_name='alumnoFoto', db_column='alumno_id', on_delete=models.PROTECT
    )
    
    class Meta:
        db_table ='fotos'



    