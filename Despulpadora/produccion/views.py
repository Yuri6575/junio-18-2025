from rest_framework import generics
from .models import producto
from .serealizers import productoSerializer
# Importar pandas
import pandas as pd
# Importar matplotlib
import matplotlib.pyplot as plt

class productoList(generics.ListCreateAPIView):
    queryset = producto.objects.all()
    serializer_class = productoSerializer 
    
class productoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = producto.objects.all()
    serializer_class = productoSerializer


# datos de producción
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

# Estadísticas por operador
estadisticas_operador = df.groupby('Operador').agg({
    'Fruta_Procesada_kg': ['sum', 'mean', 'max'],
    'Rendimiento': 'mean',
    'Productividad': 'mean'
})
print("\nEstadísticas por operador:")
print(estadisticas_operador)

# Producción por día de la semana
df['Dia_Semana'] = df['Fecha'].dt.day_name()
produccion_diaria = df.groupby('Dia_Semana')['Pulpa_Obtenida_kg'].mean()
print("\nProducción promedio por día de la semana:")
print(produccion_diaria)

# Gráfico de producción diaria
df.plot(x='Fecha', y='Pulpa_Obtenida_kg', kind='bar', title='Producción diaria de pulpa')
plt.ylabel('Kg de pulpa')
plt.show()

# Gráfico de rendimiento por operador
df.groupby('Operador')['Rendimiento'].mean().plot(kind='pie', autopct='%1.1f%%', title='Rendimiento promedio por operador')
plt.show()