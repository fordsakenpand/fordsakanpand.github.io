from django.shortcuts import render
from .models import Administrador

# Create your views here.
def login (request):
    return render(request,'core/login.html')

def inicio (request):
    nombre=Administrador.objects.all()
    datos={
        'usuario':nombre()
    }
    if request.method== 'POST':
        formulario = nombre(request.POST)
        if formulario.is_valid:
            formulario.save()
    return render(request, 'core/inicio.html',datos)


