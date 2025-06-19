from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad_actual = models.IntegerField()
    ubicacion = models.CharField(max_length=6)
    estado = models.CharField(max_length=10)
    
def __str__(self):
        return self.nombre