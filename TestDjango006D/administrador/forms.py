from django import forms
from django.db.models.base import Model 
from django.forms import ModelForm, fields
from .models import Administrador

class formclass(ModelForm):

    class Meta:
        model = Administrador
        fields =['useradmin','contra']