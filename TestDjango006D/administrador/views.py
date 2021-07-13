from django.shortcuts import render
from .models import Administrador

# Create your views here.
def login (request):
    return render(request,'core/login.html')

def inicio (request):
    nombre=Administrador.objects.all()
    datos={
        'usuario':nombre
    }
    return render(request, 'core/inicio.html',datos)


