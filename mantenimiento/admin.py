from django.contrib import admin
from mantenimiento.models import Mantenimiento

# Register your models here.

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    pass


