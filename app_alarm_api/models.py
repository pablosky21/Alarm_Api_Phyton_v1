from django.db import models

# Create your models here.

class AlarmUserComunidad(models.Model):
    alarm_comunidadalarm_comunidad = models.ForeignKey('AlarmComunidad', models.DO_NOTHING)
    alarm_usuariosalarm_id_user = models.ForeignKey('AlarmUsuarios', models.DO_NOTHING,
                                                    db_column='alarm_usuariosalarm_id_user')
    alarm_rolalarm_idrol = models.ForeignKey('AlarmRol', models.DO_NOTHING, db_column='alarm_rolalarm_idrol')

class AlarmRol(models.Model):
    alarm_idrol = models.AutoField(primary_key=True)
    alarm_descripcion = models.IntegerField(blank=True, null=True)

class AlarmDatosEmergencia(models.Model):
    alarm_id_datos = models.AutoField(primary_key=True)
    alarm_numero_emerge = models.CharField(max_length=255, blank=True, null=True)

class AlarmCordanadas(models.Model):
    alarm_id_coordena = models.AutoField(primary_key=True)
    alarm_number = models.CharField(max_length=255, blank=True, null=True)
    alarm_comunidadalarm_comunidad = models.ForeignKey('AlarmComunidad', models.DO_NOTHING)

class AlarmComunidad(models.Model):
    alarm_comunidad_id = models.AutoField(primary_key=True)
    alarm_descripcion = models.IntegerField(blank=True, null=True)
    alarm_total_personas = models.IntegerField(blank=True, null=True)

class AlarmUsuarios(models.Model):
    alarm_id_user = models.AutoField(primary_key=True)
    alarm_correo = models.CharField(max_length=255)
    alarm_nombre = models.CharField(max_length=255, blank=True, null=True)
    alarm_apelldio = models.CharField(max_length=255, blank=True, null=True)
    alarm_usuario = models.CharField(max_length=255, blank=True, null=True)
    alar_edad = models.IntegerField(blank=True, null=True)

    def NombreUsuario(self):
        cadena="{0}"
        return cadena.format(self.alarm_nombre)
    def __str__(self):
        return self.NombreUsuario()

class Profesor(models.Model):
    Apellido = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Rut = models.CharField(max_length=20)
    FechaNacimiento = models.DateField()

class Alumno(models.Model):
    Apellido=models.CharField(max_length=35)
    Nombres=models.CharField(max_length=35)
    Rut=models.CharField(max_length=20)
    FechaNacimiento=models.DateField()
















            # class Matricula(models.Model):
    #     Alumno = models.ForeignKey(Alumno ,null=False,blank=False,on_delete=models.CASCADE())