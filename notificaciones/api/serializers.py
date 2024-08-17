from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from notificaciones.models import Notificacion  # Asegúrate de importar tu modelo Consultorio aquí\



class NotificacionesSerializer(ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
