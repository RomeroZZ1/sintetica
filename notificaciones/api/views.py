from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from notificaciones.api.serializers import NotificacionesSerializer
from notificaciones.models import Notificacion

class NotificacionApiViewSet(ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionesSerializer
    permission_classes = [IsAdminUser]