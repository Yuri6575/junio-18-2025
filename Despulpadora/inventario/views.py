from rest_framework import generics
from .models import stock
from .serealizers import stockSerializer



class stockList(generics.ListCreateAPIView):
    queryset = stock.objects.all()
    serializer_class = stockSerializer 
    
class stockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = stock.objects.all()
    serializer_class = stockSerializer
