from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from canchas.models import Cancha  # Asegúrate de importar tu modelo Consultorio aquí\


class CanchaSerializer(ModelSerializer):
    estado_actual = serializers.SerializerMethodField()

    class Meta:
        model = Cancha
        fields = '__all__'

    def get_estado_actual(self, obj):
        # Evaluando el estado actual de la cancha
        if obj.estado == 'DISPONIBLE':
            return 'Disponible'
        elif obj.estado == 'RESERVADA':
            return 'Reservada'
        elif obj.estado == 'MANTENIMIENTO':
            return 'En Mantenimiento'
        else:
            return 'Estado desconocido'