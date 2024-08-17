from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from reservas.api.serializers import ReservasSerializer, ReservaConjuntaSerializer
from reservas.models import Reserva, ReservaConjunta, ColaSolo

class ReservasApiViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [IsAdminUser]

class ReservaConjuntaApiViewSet(ModelViewSet):
    queryset = ReservaConjunta.objects.all()
    serializer_class = ReservaConjuntaSerializer
    permission_classes = [IsAdminUser]


class ReservaSoloApiViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        # Obtén el usuario del request
        usuario = self.request.user

        # Extrae el ID de la cancha desde los datos validados
        cancha_id = self.request.data.get('id_cancha')

        # Añade al usuario a la cola
        ColaSolo.objects.create(id_usuario=usuario, id_cancha_id=cancha_id)

        # Verifica si la cola está completa
        if ColaSolo.verificar_equipo_completo(cancha_id):
            anfitrion = ColaSolo.obtener_anfitrion(cancha_id)
            # Notifica a los usuarios
            mensaje = f"El equipo está completo para {anfitrion.id_cancha.nombre}. Esperando a que el anfitrión programe la hora."
            anfitrion.notificar_usuarios(mensaje)

        # Aquí puedes continuar con la creación de la reserva si fuera necesario
        super().perform_create(serializer)