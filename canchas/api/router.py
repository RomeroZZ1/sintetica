from django.db import router
from rest_framework.routers import DefaultRouter

from canchas.api.views import CanchasApiViewSet



router_canchas = DefaultRouter()

router_canchas.register(prefix='canchas', basename='canchas', viewset=CanchasApiViewSet)




