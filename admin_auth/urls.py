from django.urls import path
from admin_auth.views import admin_login_view, verifica_admin_view, admin_logout, registro_usuario_view

urlpatterns = [
    path('acceso-administrativo/', admin_login_view, name='admin_login_view'),
    path('verifica-administrador/', verifica_admin_view, name='verifica_admin_view'),
    path('cerrar-sesion/', admin_logout, name='admin_logout'),
    path('registrarse/', registro_usuario_view, name='registro_usuario_view'),
]