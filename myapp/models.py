from django.db import models


class Canchas(models.Model):
    nombre = models.CharField(max_length=50)
    deporte = models.CharField(max_length=50)
    reserva = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre} - {self.deporte}'

class Horario(models.Model):
    cancha = models.ForeignKey(Canchas, related_name='horarios', on_delete=models.CASCADE)
    fecha = models.CharField(max_length=20)
    horarios = models.TextField(max_length=50, default='')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.fecha} - {self.horarios}'

class DatosPersona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='persona')
    cancha = models.ForeignKey(Canchas, on_delete=models.CASCADE, related_name='persona')

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.telefono} - {self.email}'
