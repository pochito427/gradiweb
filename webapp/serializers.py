from rest_framework import serializers
from . models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = {'id', 'nombre', 'descripcion', 'url_imagen', 'dias_semana'}
