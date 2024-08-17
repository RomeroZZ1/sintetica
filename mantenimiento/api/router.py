from django.db import router
from rest_framework.routers import DefaultRouter

from mantenimiento.api.views import MantenimientoApiViewSet



router_mantenimiento = DefaultRouter()

router_mantenimiento.register(prefix='mantenimiento', basename='mantenimiento', viewset=MantenimientoApiViewSet)




