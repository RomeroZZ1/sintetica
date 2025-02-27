from datetime import datetime, timedelta
from django.utils import timezone 
from django.db import models
from usuarios.models import Usuarios
from canchas.models import Cancha

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField(editable=False)

    def save(self, *args, **kwargs):
        # Calcula la hora_fin automáticamente
        if self.hora_inicio:
            hora_inicio_dt = datetime.combine(datetime.today(), self.hora_inicio)
            hora_fin_dt = hora_inicio_dt + timedelta(hours=1)
            self.hora_fin = hora_fin_dt.time()

        # Verifica si la cancha está en mantenimiento
        if self.id_cancha.estado == 'Mantenimiento':
            raise ValueError("La cancha está en mantenimiento y no se puede reservar.")

        # Verifica disponibilidad de la cancha
        if Reserva.objects.filter(
            id_cancha=self.id_cancha,
            hora_inicio__lt=self.hora_fin,
            hora_fin__gt=self.hora_inicio
        ).exists():
            raise ValueError("La cancha ya está reservada en ese horario.")
        
        # Si todo está bien, cambia el estado de la cancha a "Reservada"
        self.id_cancha.reservar()
        super().save(*args, **kwargs)

        #####
        self.notificar_usuarios(f'Partido programado a las {self.hora_inicio}')######################
        super().save(*args, **kwargs)
        ####

    def delete(self, *args, **kwargs):
        # Cambia el estado de la cancha a "Disponible" cuando la reserva se elimina
        self.id_cancha.liberar()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'Reserva {self.id_reserva} - Por {self.id_usuario} - {self.hora_inicio} - En {self.id_cancha}'
    
    #####
    def notificar_usuarios(self, mensaje):
        """Envía notificaciones a todos los usuarios en la cola."""
        jugadores_en_cola = ColaSolo.objects.filter(id_cancha=self.id_cancha)
        for jugador in jugadores_en_cola:
            Notificacion.objects.create(id_usuario=jugador.id_usuario, mensaje=mensaje)

    #####

class ReservaConjunta(models.Model):
    id_reserva_conjunta = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    nombre_grupo = models.CharField(max_length=100)
    numero_participantes = models.IntegerField()
    
    def __str__(self):
        return self.nombre_grupo
    

########################################################################

class ColaSolo(models.Model):
    id_cola = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    unido_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['unido_en']

    def __str__(self):
        return f'Usuario {self.id_usuario} en cola para {self.id_cancha}'

    @classmethod
    def verificar_equipo_completo(cls, id_cancha):
        """Verifica si la cola ya tiene 6 jugadores."""
        return cls.objects.filter(id_cancha=id_cancha).count() >= 6

    @classmethod
    def obtener_anfitrion(cls, id_cancha):
        """Obtiene el primer usuario en la cola (el anfitrión)."""
        return cls.objects.filter(id_cancha=id_cancha).order_by('unido_en').first()

    @classmethod
    def limpiar_cola(cls, id_cancha):
        """Limpia la cola después de que se ha programado un partido."""
        cls.objects.filter(id_cancha=id_cancha).delete()


class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    mensaje = models.TextField()
    enviado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Notificación para {self.id_usuario} en {self.enviado_en}'


    

    

