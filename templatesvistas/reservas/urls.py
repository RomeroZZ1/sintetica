from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('reservar/', views.reservar, name='reservar'),  # Página para reservar
    path('historial/', views.historial, name='historial'),  # Historial de reservas
]
