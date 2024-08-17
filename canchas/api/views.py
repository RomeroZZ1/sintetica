from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from canchas.api.serializers import CanchaSerializer
from canchas.models import Cancha

class CanchasApiViewSet(ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer
    permission_classes = [IsAdminUser]