from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from usuarios.models import Usuarios

# Register your models here.

@admin.register(Usuarios)
class UsuariosAdmin(BaseUserAdmin):
    pass
