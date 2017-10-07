from django.db import models

# Create your models here.

class Alumno(models.Model):
    Apellido=models.CharField(max_length=35)
    Nombres=models.CharField(max_length=35)
    Rut=models.CharField(max_length=20)
    FechaNacimiento=models.DateField()

    # class Matricula(models.Model):
    #     Alumno = models.ForeignKey(Alumno ,null=False,blank=False,on_delete=models.CASCADE())