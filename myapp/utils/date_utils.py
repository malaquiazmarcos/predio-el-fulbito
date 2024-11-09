from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'Spanish_Spain')

def siete_dias():
    lista_dias = []

    for x in range(7):
        fecha = datetime.now() + timedelta(days=x)
        formato_fecha = fecha.strftime('%A %d-%m-%Y')
        lista_dias.append(formato_fecha)

    return lista_dias





