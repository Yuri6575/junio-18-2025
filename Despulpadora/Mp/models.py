from django.db import models

# se crea las clases para los modelos de la Materia primaria Fruta

class Fruta(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_kl = models.IntegerField()
    proveedor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
