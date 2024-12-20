from django.shortcuts import render, redirect
from myapp.models import Canchas, DatosReserva, Telefono, Horario
from django.contrib.auth.models import User
from myapp.utils.date_utils import siete_dias
from django.contrib.auth.decorators import login_required
import ast

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
    lista_dias = siete_dias()

    canchas = Canchas.objects.all()

    return render(request, 'myapp/paddel.html', {
        'lista_dias' : lista_dias,
        'canchas' : canchas
    })

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
    
    fecha_seleccionada = request.POST.get('fecha')
    horarios_queryset = Horario.objects.filter(fecha=fecha_seleccionada, cancha_id=id)
    
    horarios_reservados = []
    for reserva in horarios_queryset:
        horarios = ast.literal_eval(reserva.horarios)  # ast convierte "[lista]" en [lista] (de string a lista literal)
        horarios_reservados.append(horarios)
    
    return render(request, 'myapp/horarios.html', {
        'id' : id,
        'fecha_seleccionada' : fecha_seleccionada,
        'lista_horarios' : lista_horarios, 
        'horarios_reservados' : horarios_reservados
    })

@login_required(login_url='admin_login_view')
def confirmar_reserva_view(request, id):
    horario_seleccionado = request.POST.getlist('horario')
    if not horario_seleccionado:
        lista_horarios = [
        '17:00-18:00',
        '18:00-19:00',
        '19:00-20:00',
        '20:00-21:00',
        '21:00-22:00',
        '22:00-23:00',
        '23:00-00:00',
        ]
        fecha_seleccionada = request.POST.get('fecha')
        horarios_queryset = Horario.objects.filter(fecha=fecha_seleccionada, cancha_id=id)
        
        horarios_reservados = []
        for reserva in horarios_queryset:
            horarios = ast.literal_eval(reserva.horarios)  # ast convierte "[lista]" en [lista] (de string a lista literal)
            horarios_reservados.append(horarios)

        return render(request, 'myapp/horarios.html', {
        'id' : id,
        'fecha_seleccionada' : fecha_seleccionada,
        'lista_horarios' : lista_horarios, 
        'horarios_reservados' : horarios_reservados
        })
    
    else:
        fecha_seleccionada = request.POST.get('fecha')
        request.session['horario_seleccionado'] = horario_seleccionado
        request.session['fecha_seleccionada'] = fecha_seleccionada

        datos_usuario = request.user
        datos_telefono = Telefono.objects.filter(user=datos_usuario).first()

        if datos_telefono:
            telefono = datos_telefono.telefono
        else:
            telefono = None

        return render(request, 'myapp/confirmacion.html', {
            'id' : id,
            'datos_usuario' : datos_usuario,
            'telefono' : telefono,
        })

@login_required(login_url='admin_login_view')
def confirmar_reserva_2_view(request, id):
    cancha_instancia = Canchas.objects.get(id=id)
    user_id = request.user.id
    usuario_instancia = User.objects.get(id=user_id)
    datos_usuario = request.user
    actualiza_telefono = Telefono.objects.filter(user=datos_usuario).first()
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email') 

        if (nombre and apellido and telefono and email):
            try:
                horario_seleccionado = request.session.get('horario_seleccionado')
                fecha_seleccionada = request.session.get('fecha_seleccionada')

                reserva = Horario(
                cancha=cancha_instancia,
                fecha=fecha_seleccionada,
                horarios=horario_seleccionado,
                disponible=False
                )
                reserva.save()

                horario_id = reserva.id

                horario_instancia = Horario.objects.get(id=horario_id)

                datos_reserva = DatosReserva(
                    cancha_id=cancha_instancia.id,
                    horario_id=horario_instancia.id ,
                    user_id=user_id
                )
                datos_reserva.save()

                if actualiza_telefono:
                    actualiza_telefono.telefono = telefono
                    actualiza_telefono.save()
                else:
                    actualiza_telefono = Telefono(
                        user=usuario_instancia,
                        telefono=telefono
                    )
                    actualiza_telefono.save()

                datos_usuario.first_name = nombre
                datos_usuario.last_name = apellido
                datos_usuario.email = email
                datos_usuario.save()

            except Exception as e:
                print(f'ERROR: {e}')

        return redirect('index')