from django.urls import path
from appvet.views import *

urlpatterns = [
    path('inicio/', vista_inicio, name="vet-inicio"),
    path('clientes/', vista_clientes, name="vet-clientes"),
    path('mascotas/', vista_mascotas, name="vet-mascotas"),
    path('productos/', vista_productos, name="vet-productos"),
]