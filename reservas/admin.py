from django.contrib import admin
from reservas.models import Reserva

# Register your models here.


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    pass