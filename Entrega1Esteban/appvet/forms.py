from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(min_length=3,max_length=20) #se puede poner maximo y minimo para validar en el formulario
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