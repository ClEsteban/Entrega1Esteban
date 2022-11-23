from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.especie.capitalize()} - {self.nombre} -  Raza: {self.raza.upper()} - Edad: {self.edad}"

class Producto(models.Model):
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
