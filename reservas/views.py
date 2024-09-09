from django.shortcuts import render

def home(request):
    return render(request, 'reservas/home.html')

def reservar(request):
    if request.method == 'POST':
        # Lógica para procesar la reserva
        pass
    return render(request, 'reservas/reservar.html')

def historial(request):
    # Lógica para obtener el historial de reservas del usuario
    return render(request, 'reservas/historial.html')
