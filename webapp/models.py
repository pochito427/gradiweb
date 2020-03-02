from django.db import models

# Create your models here.
class Servicio(models.Model):
    id_servicio = models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    url_imagen = models.URLField(max_length=255)
    dias_semana = models.CharField(max_length=32)
