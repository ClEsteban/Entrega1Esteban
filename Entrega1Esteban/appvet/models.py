from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.DateField()

class Producto(models.Model):
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
