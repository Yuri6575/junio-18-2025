from rest_framework import generics
from .models import Fruta
from .serealizers import FrutaSerializer



class FrutaList(generics.ListCreateAPIView):
    queryset = Fruta.objects.all()
    serializer_class = FrutaSerializer 
    
class FrutaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruta.objects.all()
    serializer_class = FrutaSerializer

