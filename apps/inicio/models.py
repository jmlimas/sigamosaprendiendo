from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=180)
    edad = models.IntegerField()
    colonia = models.CharField(max_length=100)
    direccion = models.CharField(max_length=140)
    municipio = models.CharField(max_length=140)
    telefono = models.CharField(max_length=15, null=True)
    celular = models.CharField(max_length=10, null=True)
    grado = models.CharField(max_length=80)
    escuela = models.CharField(max_length=200)
    tutor = models.CharField(max_length=180)
    Comentario = models.TextField(max_length=700)
    foto = models.ImageField(upload_to='foto_alumno')
    hospital = models.CharField(max_length=100)


    def __unicode__(self):
        return self.nombre    