from django.urls import path
from .views import productoList, productoDetail

urlpatterns = [
    path('produccion/', productoList.as_view()),
    path('produccion/<int:pk>/', productoDetail.as_view()),
]