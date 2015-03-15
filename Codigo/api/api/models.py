from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=26)

    class Meta:
        db_table = u'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey('AuthGroup')
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        db_table = u'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=33)

    class Meta:
        db_table = u'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=42)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = u'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AuthUser')
    group = models.ForeignKey('AuthGroup')

    class Meta:
        db_table = u'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AuthUser')
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        db_table = u'auth_user_user_permissions'


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, db_column=u'idCategoria')
    nombre = models.CharField(max_length=15, db_column=u'Nombre', blank=True)

    class Meta:
        db_table = u'categoria'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, db_column=u'idCliente')
    nombre = models.CharField(max_length=15, db_column=u'Nombre', blank=True)
    usuario = models.CharField(max_length=15, db_column=u'Usuario', blank=True)
    email = models.CharField(max_length=30, db_column=u'Email', blank=True)
    contrase_a = models.CharField(max_length=15, db_column=u'Contrase\xf1a', blank=True)
    sexo = models.IntegerField(null=True, db_column=u'Sexo', blank=True)
    administrador = models.IntegerField(null=True, db_column=u'Administrador', blank=True)

    class Meta:
        db_table = u'cliente'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=66)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    user = models.ForeignKey('AuthUser')

    class Meta:
        db_table = u'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=33)
    app_label = models.CharField(max_length=33)
    model = models.CharField(max_length=33)

    class Meta:
        db_table = u'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=85)
    name = models.CharField(max_length=85)
    applied = models.DateTimeField()

    class Meta:
        db_table = u'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=13, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = u'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=33)
    name = models.CharField(max_length=16)

    class Meta:
        db_table = u'django_site'


class Evento(models.Model):
    id_evento = models.IntegerField(primary_key=True, db_column=u'idEvento')
    nombre = models.CharField(max_length=15, db_column=u'Nombre', blank=True)
    fecha = models.DateField(null=True, db_column=u'Fecha', blank=True)
    hora = models.CharField(max_length=15, db_column=u'Hora', blank=True)
    descripcion = models.CharField(max_length=15, db_column=u'Descripcion', blank=True)
    email = models.CharField(max_length=15, db_column=u'Email', blank=True)
    calificacion = models.IntegerField(null=True, db_column=u'Calificacion', blank=True)
    precio = models.IntegerField(null=True, db_column=u'Precio', blank=True)
    estado = models.IntegerField(null=True, db_column=u'Estado', blank=True)
    imagen = models.TextField(null=True,db_column=u'Imagen', blank=True)
    lugar_id_lugar = models.ForeignKey('Lugar', db_column=u'Lugar_idLugar')
    categoria_id_categoria = models.ForeignKey('Categoria', db_column=u'Categoria_idCategoria')
    cliente_id_cliente = models.ForeignKey('Cliente', db_column=u'Cliente_idCliente')

    class Meta:
        db_table = u'evento'


class Lugar(models.Model):
    id_lugar = models.IntegerField(primary_key=True, db_column=u'idLugar')
    nombre = models.CharField(max_length=15, db_column=u'Nombre', blank=True)
    direccion = models.CharField(max_length=15, db_column=u'Direccion', blank=True)

    class Meta:
        db_table = u'lugar'


class Miseventos(models.Model):
    id_mis_eventos = models.IntegerField(primary_key=True, db_column=u'idMisEventos')
    cliente_id_cliente = models.ForeignKey('Cliente', db_column=u'Cliente_idCliente')
    evento_id_evento = models.ForeignKey('Evento', db_column=u'Evento_idEvento')
    mi_puntuacion = models.IntegerField(null=True, db_column=u'MiPuntuacion', blank=True)

    class Meta:
        db_table = u'miseventos'


class Telefonos(models.Model):
    id_telefonos = models.IntegerField(primary_key=True, db_column=u'idTelefonos')
    telefono = models.CharField(max_length=15, db_column=u'Telefono', blank=True)
    evento_id_evento = models.ForeignKey('Evento', db_column=u'Evento_idEvento')

    class Meta:
        db_table = u'telefonos'
