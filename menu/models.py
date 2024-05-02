from django.db import models

# Create your models here.
class Menu(models.Model):
    NombrePlato = models.CharField(max_length=45)
    Descripcion = models.CharField(max_length=60)
    Precio = models.FloatField(max_length=55)

    def __str__(self):
        return self.NombrePlato