from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
# Create your views here.

def vista_inicio(request):
    return render(request, "appvet/inicio.html")

def vista_clientes(request):
    return render(request, "appvet/clientes.html")

def vista_mascotas(request):
    return render(request, "appvet/mascotas.html")

def vista_productos(request):
    return render(request, "appvet/productos.html")