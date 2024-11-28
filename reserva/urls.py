from django.urls import path
from reserva.views import reservas_view, cancelar_reserva_view

urlpatterns = [
    path('mis-reservas/', reservas_view, name='reservas_view'),
    path('cancelar-reserva', cancelar_reserva_view, name='cancelar_reserva_view'),
]