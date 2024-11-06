

def procesar_datos_persona(request):
    if request.method == 'POST':
        datos_persona = request.POST
        print(datos_persona)
    
    return datos_persona