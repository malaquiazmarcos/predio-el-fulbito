from django.shortcuts import render, redirect
from myapp.models import Canchas, DatosPersona, Horario
from myapp.utils.date_utils import siete_dias
from datetime import datetime

def index(request):
    
    return render(request, 'base.html')

def futbol_view(request):   
    lista_dias = siete_dias()

    canchas = Canchas.objects.all()

    return render(request, 'myapp/futbol.html', {
        'lista_dias' : lista_dias,
        'canchas' : canchas
    })

def paddel_view(request):
    return render(request, 'myapp/paddel.html')

def horarios_view(request, id):
    lista_horarios = [
        '17:00-18:00',
        '18:00-19:00',
        '19:00-20:00',
        '20:00-21:00',
        '21:00-22:00',
        '22:00-23:00',
        '23:00-00:00',
    ]
    if request.method == 'POST':
        fecha_seleccionada = request.POST.get('fecha')

    return render(request, 'myapp/horarios.html', {
        'id' : id,
        'fecha_seleccionada' : fecha_seleccionada,
        'lista_horarios' : lista_horarios
    })

def confirmar_reserva_view(request, id):
    horario_seleccionado = request.POST.getlist('horario')
    fecha_seleccionada = request.POST.get('fecha')
    
    canchas_instancia = Canchas.objects.get(id=id)
    reserva = Horario(
            cancha=canchas_instancia,
            fecha=fecha_seleccionada,
            horarios=horario_seleccionado,
            disponible=False
        )
    reserva.save()

    horario_id = reserva.id
    
    return render(request, 'myapp/confirmacion.html', {
        'id' : id, 
        'horario_id' : horario_id
    })

def confirmar_reserva_2_view(request, id):
    horario_id = request.POST.get('horario_id')

    cancha_instancia = Canchas.objects.get(id=id)
    horario_instancia = Horario.objects.get(id=horario_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email') 

        datos_persona = DatosPersona(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email, 
            horario=horario_instancia,
            cancha=cancha_instancia
        )
        datos_persona.save()
    
    return redirect('index')

