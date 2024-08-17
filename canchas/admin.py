from django.contrib import admin

from canchas.models import Cancha

# Register your models here.

@admin.register(Cancha)
class CanchasAdmin(admin.ModelAdmin):
    pass

