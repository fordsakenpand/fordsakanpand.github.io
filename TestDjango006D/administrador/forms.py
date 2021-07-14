from django import forms
from django.db.models.base import Model 
from django.forms import ModelForm, fields
from .models import Administrador,Vehiculo

class formclass(ModelForm):
    class Meta:
        model = Administrador
        fields =['useradmin','contra']

class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','maraca','modelo','Categoria']