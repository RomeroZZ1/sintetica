from django.db import router
from rest_framework.routers import DefaultRouter

from notificaciones.api.views import NotificacionApiViewSet



router_notificaciones = DefaultRouter()

router_notificaciones.register(prefix='notificaciones', basename='notificaciones', viewset=NotificacionApiViewSet)




