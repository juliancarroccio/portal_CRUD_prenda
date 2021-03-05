# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Color(models.Model):
    id_color = models.AutoField(primary_key=True)
    descripcion_color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'color'

    def __str__(self):
        return '%s' %self.descripcion_color


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


class Familia(models.Model):
    id_familia = models.AutoField(primary_key=True)
    descripcion_familia = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia'

    def __str__(self):
        return '%s' %self.descripcion_familia


class Industria(models.Model):
    id_industria = models.AutoField(primary_key=True)
    descripcion_industria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industria'

    def __str__(self):
        return '%s' %self.descripcion_industria




class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    descripcion_marca = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'

    def __str__(self):
        return '%s' %self.descripcion_marca


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    industria = models.ForeignKey(Industria, models.DO_NOTHING, db_column='id_industria', blank=True, null=True)
    color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color', blank=True, null=True)
    talle = models.ForeignKey('Talle', models.DO_NOTHING, db_column='id_talle', blank=True, null=True)
    familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    codigo_barra = models.IntegerField(db_column='codigoBarra', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField('Descripcion',db_column='descripcion_producto',max_length=1000, blank=True, null=True)
    precio = models.FloatField()
    stock = models.IntegerField()
    iva = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    descripcion_proveedor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return '%s' %self.descripcion_proveedor


class Talle(models.Model):
    id_talle = models.AutoField(primary_key=True)
    descripcion_talle = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talle'

    def __str__(self):
        return '%s' %self.descripcion_talle