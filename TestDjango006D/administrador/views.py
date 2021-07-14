from django.shortcuts import render
#from .models import Administrador
from .models import Vehiculo
# Create your views here.
def login (request):
    return render(request,'core/login.html')

#def inicio (request): 
    #nombre=Administrador.objects.all()     
    #datos={
        #'usuario':nombre()
    #}
    #if request.method== 'POST':
        #formulario = nombre(request.POST)
        #if formulario.is_valid:
        #    formulario.save()  
   # return render(request, 'core/inicio.html',datos)
    #return render(request, 'core/inicio.html')

def inicio(request):

    vehiculos = Vehiculo.objects.all()
    datos = {

        "ListaVehiculos":vehiculos
    }
    return render(request,'core/inicio.html',datos)

def form_vehiculo(request):
    datos = {
        'form': Vehiculo()
    }
    if request.method =="POST":
        formulario = Vehiculo(request.post)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "guardado correctamente"

    return render(request,'core/form_vehiculo.html',datos)