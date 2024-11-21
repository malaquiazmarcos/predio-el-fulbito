from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def admin_login_view(request):

    return render(request, 'admin_auth/admin_login.html')

def verifica_admin_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        passwrd = request.POST.get('passwrd')

        user = authenticate(request, username=usuario, password=passwrd)

        if user is not None:
            login(request, user)
            print('usuario iniciado correctamente')
            return redirect('index')
        else:
            print('error')
            return redirect('admin_login_view')

    return redirect('index')

def admin_logout(request):
    logout(request)

    return redirect('index')

def registro_usuario_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        email = request.POST.get('email') 
        passwrd = request.POST.get('passwrd') 
        confirm_passwrd = request.POST.get('confirm_passwrd')

        if passwrd != confirm_passwrd:
            messages.error(request, 'Las contraseñas no coinciden.')
            print('Las contraseñas no coinciden.')
            return render(request, 'admin_auth/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ingresado ya esta registrado.')
            print('el email ya existe en la base de datos')
            return render(request, 'admin_auth/register.html')
        
        nuevo_usuario = User(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=passwrd
        )
        nuevo_usuario.set_password(passwrd)
        nuevo_usuario.save()

        login(request, nuevo_usuario)
        print('Se ha creado un nuevo usuario')
        messages.success(request, 'Usuario registrado exitosamente.')
        return redirect('index')

    return render(request, 'admin_auth/register.html')