from rest_framework import generics
from .models import producto
from .serealizers import productoSerializer
# Importar pandas
import pandas as pd


class productoList(generics.ListCreateAPIView):
    queryset = producto.objects.all()
    serializer_class = productoSerializer 
    
class productoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = producto.objects.all()
    serializer_class = productoSerializer


# Ejemplo de datos de producción
data = {
    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Fruta_Procesada_kg': [1200, 1500, 900, 1800, 1300],
    'Pulpa_Obtenida_kg': [840, 1050, 630, 1260, 910],
    'Horas_Operacion': [8, 10, 6, 12, 9],
    'Desperdicio_kg': [360, 450, 270, 540, 390],
    'Operador': ['Juan', 'Pedro', 'Juan', 'Maria', 'Pedro']
}

df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'])  # Convertir a formato de fecha

# Estadísticas descriptivas básicas
resumen = df.describe()
print("Estadísticas descriptivas básicas:")
print(resumen)

# Rendimiento (pulpa/fruta)
df['Rendimiento'] = df['Pulpa_Obtenida_kg'] / df['Fruta_Procesada_kg'] * 100

# Productividad (pulpa/hora)
df['Productividad'] = df['Pulpa_Obtenida_kg'] / df['Horas_Operacion']