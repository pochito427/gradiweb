from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    url_imagen = models.URLField(max_length=255)
    dias_semana = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre

