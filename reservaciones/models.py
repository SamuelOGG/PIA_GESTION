from django.db import models

# Create your models here.
class Reservaciones(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=60)
    Correo = models.EmailField(max_length = 254)
    Telefono = models.CharField(max_length=50)
    NoPersonas = models.PositiveIntegerField(null=True)  # Cambiado a PositiveIntegerField
    FechaReserva = models.DateField(null=True)  # Cambiado a DateField
    HoraReserva = models.TimeField(null=True)
    codigo_unico = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.Nombre} {self.Apellidos}"