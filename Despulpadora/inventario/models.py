from django.db import models

class stock(models.Model):
    producto = models.CharField(max_length=50)
    cantidad_inicial= models.IntegerField()
    cantidad_actual = models.IntegerField()
    
    
def __str__(self):
        return self.producto
