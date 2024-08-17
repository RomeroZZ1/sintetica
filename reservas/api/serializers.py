from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from reservas.models import Reserva, ReservaConjunta  # Asegúrate de importar tu modelo Consultorio aquí\



class ReservasSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ReservaConjuntaSerializer(ModelSerializer):
    class Meta:
        model = ReservaConjunta
        fields = '__all__'



