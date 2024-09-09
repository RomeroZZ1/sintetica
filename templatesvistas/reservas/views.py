from django.shortcuts import render

def home(request):
    return render(request, 'reservas/home.html')

def reservar(request):
    return render(request, 'reservas/reservar.html')

def historial(request):
    return render(request, 'reservas/historial.html')
