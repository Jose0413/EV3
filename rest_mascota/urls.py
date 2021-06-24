from django.urls import path
from rest_mascota. views import lista_mascotas

urlpatterns = [
    path('lista_mascotas', lista_mascotas, name='lista_mascotas'),
]
