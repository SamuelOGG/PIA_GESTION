from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Reservaciones
import random
import string

def reservar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        personas = request.POST.get('cantidad_personas')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        # Generar un código aleatorio único
        codigo_unico = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        # Verificar si ya existe una reserva con el mismo código único en la base de datos
        reserva_existente = Reservaciones.objects.filter(codigo_unico=codigo_unico).first()
        while reserva_existente:
            # Si el código ya existe, generar otro código único nuevo
            codigo_unico = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            reserva_existente = Reservaciones.objects.filter(codigo_unico=codigo_unico).first()

        # Guardar los datos en la base de datos junto con el código único
        reserva = Reservaciones(Nombre=nombre, Apellidos=apellidos, Correo=correo, Telefono=telefono,
                                NoPersonas=personas, FechaReserva=fecha, HoraReserva=hora, codigo_unico=codigo_unico)
        reserva.save()

        # Renderizar la plantilla del ticket de reservación
        return render(request, 'ticket.html', {'reserva': reserva})
    else:
        # Eliminar el código único de la sesión al solicitar la página de ticket
        if 'codigo_unico' in request.session:
            del request.session['codigo_unico']
        return render(request, 'ticket.html')
