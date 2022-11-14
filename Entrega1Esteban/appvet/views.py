from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from appvet.models import *
from appvet.forms import *

# Create your views here.

def vista_inicio(request):
    return render(request, "appvet/inicio.html")

def vista_clientes(request):
    return render(request, "appvet/clientes.html")


def vista_crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        #validamos que el formulario no tenga problemas
        if formulario.is_valid():
        #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            cliente = Cliente(nombre = data["nombre"], telefono = data["telefono"])

            cliente.save()
 
    formulario = ClienteFormulario()

    contexto = {"formulario": formulario}
    return render(request, "appvet/crear_cliente.html", contexto)


def vista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "appvet/mascotas.html", {"mascota":mascotas})

def vista_crear_mascota(request):
    if request.method == "POST":
        formulario = MascotaFormulario(request.POST)

        #validamos que el formulario no tenga problemas
        if formulario.is_valid():
        #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            cliente = Mascota(nombre = data["nombre"], especie = data["especie"], raza = data["raza"], edad = data["edad"])

            cliente.save()
 
    formulario = MascotaFormulario()

    contexto = {"formulario": formulario}
    return render(request, "appvet/crear_mascota.html",contexto)

def vista_productos(request):
    productos = Producto.objects.all()
    return render(request, "appvet/productos.html", {"producto":productos})

def vista_crear_producto(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)

        #validamos que el formulario no tenga problemas
        if formulario.is_valid():
        #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            cliente = Producto(tipo = data["tipo"], marca = data["marca"], precio = data["precio"])

            cliente.save()
 
    formulario = ProductoFormulario()

    contexto = {"formulario": formulario}
    return render(request, "appvet/crear_producto.html", contexto)

def vista_buscador(request):
    return render(request, "appvet/buscador.html")