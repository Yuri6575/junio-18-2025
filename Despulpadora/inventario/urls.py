from django.urls import path
from .views import stockList, stockDetail

urlpatterns = [
    path('inventario/', stockList.as_view()),
    path('inventario/<int:pk>/', stockDetail.as_view()),
]