# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User

class UsuarioManager(BaseUserManager):
  '''Manager para perfiles de usuario'''
  def create_user(self, email, name, password=None):
    ''' Crear nuevo usuario '''
    if not email:
      raise ValueError('Usuario deber tener un correo')

    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, email, name, password):
    user = self.create_user(email, name, password)

    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)

    def __str__(self):
      return self.nombre

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    tienda = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    estado = models.IntegerField()
    fecharegistro = models.DateTimeField(db_column='fechaRegistro')  # Field name made lowercase.
    ciudad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'


class Detallepedido(models.Model):
    iddetalle = models.AutoField(db_column='idDetalle', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField()
    precio = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    idpedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='idPedido')  # Field name made lowercase.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detallepedido'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empaque(models.Model):
    idempaque = models.AutoField(db_column='idEmpaque', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)

    def __str__(self):
      return self.nombre

    class Meta:
        managed = False
        db_table = 'empaque'


class Pedido(models.Model):
    idpedido = models.AutoField(db_column='idPedido', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(max_length=10)
    fechapedido = models.DateTimeField(db_column='fechaPedido')  # Field name made lowercase.
    ahorro = models.FloatField()
    subtotal = models.FloatField()
    ivatotal = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    idvendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='idVendedor')  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.

    def __str__(self):
      return self.estado

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    precio = models.FloatField(blank=True, null=True)
    fechaingreso = models.DateTimeField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    iva = models.FloatField(blank=True, null=True)
    idunidad = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='idUnidad')  # Field name made lowercase.
    idempaque = models.ForeignKey(Empaque, models.DO_NOTHING, db_column='idEmpaque')  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idCategoria')  # Field name made lowercase.

    def __str__(self):
      return self.nombre

    class Meta:
        managed = False
        db_table = 'producto'


class Rol(models.Model):
    idrol = models.AutoField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)

    def __str__(self):
      return self.nombre

    class Meta:
        managed = False
        db_table = 'rol'


class UnidadMedida(models.Model):
    idunidad = models.AutoField(db_column='idUnidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    valor = models.FloatField(blank=True, null=True)

    def __str__(self):
      return self.nombre

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class Usuario(models.Model): # AbstractBaseUser, PermissionsMixin
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    ruc = models.CharField(max_length=13)
    cedula = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=250) #models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro')  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='idRol')  # Field name made lowercase.
    idvendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='idVendedor')  # Field name made lowercase.

    objects = UsuarioManager();

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
      '''Obtener nombre completo del usuario'''
      return self.name

    def get_short_name(self):
      '''Obtener nombre corto'''
      return self.name

    def __str__(self):
      return self.correo #+ ' ' +self.apellidos

    class Meta:
        managed = False
        db_table = 'usuario'


class Vendedor(models.Model):
    idvendedor = models.AutoField(db_column='idVendedor', primary_key=True)  # Field name made lowercase.
    numventas = models.IntegerField(db_column='numVentas')  # Field name made lowercase.

    def __str__(self):
      return str(self.idvendedor)

    class Meta:
        managed = False
        db_table = 'vendedor'
