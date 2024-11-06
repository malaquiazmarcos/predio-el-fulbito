from django.urls import path
from myapp.views import futbol_view, paddel_view, index, horarios_view, confirmar_reserva_view, confirmar_reserva_2_view

urlpatterns = [
    path('', index, name='index'),
    path('paddel/', paddel_view, name='paddel_view'), 
    path('futbol/', futbol_view, name='futbol_view'),
    path('horarios/<int:id>', horarios_view, name='horarios_view'),
    path('confirmar-reserva/<int:id>', confirmar_reserva_view, name='confirmar_reserva_view'),
    path('confirmar-reserva-2/<int:id>', confirmar_reserva_2_view, name='confirmar_reserva_2_view')
]