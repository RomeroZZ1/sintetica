from django.db import models
from usuarios.models import Usuarios
from django.utils import timezone

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='notificaciones_generales')
    mensaje = models.TextField()
    enviado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Notificación para {self.id_usuario} en {self.enviado_en}'
