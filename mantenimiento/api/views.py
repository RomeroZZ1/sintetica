from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from mantenimiento.api.serializers import MantenimientoSerializer
from mantenimiento.models import Mantenimiento

class MantenimientoApiViewSet(ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer
    permission_classes = [IsAdminUser]