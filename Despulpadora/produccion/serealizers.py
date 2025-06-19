from rest_framework import serializers
from .models import producto

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['nombre', 'cantidad_actual', 'ubicacion', 'estado']