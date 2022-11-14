from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()

class MascotaFormulario(forms.Form):
    nombre = forms.CharField()
    especie = forms.CharField()
    raza = forms.CharField()
    edad = forms.IntegerField()

class ProductoFormulario(forms.Form):
    tipo = forms.CharField()
    marca = forms.CharField()
    precio = forms.IntegerField()