from django.urls import path
from appvet.views import *

urlpatterns = [
    path('inicio/', vista_inicio, name="vet-inicio"),
    path('clientes/', vista_clientes, name="vet-clientes"),
    path('clientes/crear/', vista_crear_cliente, name="vet-crear-cliente"),
    path('mascotas/', vista_mascotas, name="vet-mascotas"),
    path('mascotas/crear/', vista_crear_mascota, name="vet-crear-mascota"),
    path('productos/', vista_productos, name="vet-productos"),
    path('productos/crear/', vista_crear_producto, name="vet-crear-producto"),
    path('buscador/', vista_buscador, name="vet-buscador"),
]