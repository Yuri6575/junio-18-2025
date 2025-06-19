from django.urls import path
from .views import FrutaList, FrutaDetail

urlpatterns = [
    path('frutas/', FrutaList.as_view()),
    path('frutas/<int:pk>/', FrutaDetail.as_view()),
]