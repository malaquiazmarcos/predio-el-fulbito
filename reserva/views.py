from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import *

@login_required(login_url='admin_login_view')
def reservas_view(request):
    user_instancia = request.user
    reserva_instancia = DatosReserva.objects.filter(user_id=user_instancia).select_related('horario')

    if request.user.is_staff or request.user.is_superuser:
        reservas_instancia_admin = DatosReserva.objects.all()
        telefono_instancia = Telefono.objects.all()
        print(reservas_instancia_admin) 
        print(telefono_instancia)


    return render(request, 'reservas/mis_reservas.html', {
        'reserva_instancia' : reserva_instancia,
        'reservas_instancia_admin' : reservas_instancia_admin,
        'telefono_instancia' : telefono_instancia
    })

@login_required(login_url='admin_login_view')
def cancelar_reserva_view(request):
    id_horario = request.POST.get('horario_id')
    instancia_horario = Horario.objects.get(id=id_horario)
    instancia_horario.delete()

    return redirect(request.META.get('HTTP_REFERER', 'reservas_view'))
