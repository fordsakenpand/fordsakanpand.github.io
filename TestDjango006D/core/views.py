from django.shortcuts import render

# Create your views here.
def Index (request):
    return render(request,'core/Index.html')
def Cambios (request):
    return render(request,'core/Cambios.html')
def Contacto (request):
    return render(request,'core/Contacto.html')
def Electricidad (request):
    return render(request,'core/Electricidad.html')
def Index (request):
    return render(request,'core/Index.html')
def MecaCam (request):
    return render(request,'core/MecaCam.html')
def MecaSus (request):
    return render(request,'core/MecaSus.html')
def MecaEle (request):
    return render(request,'core/MecaEle.html')
def Registro (request):
    return render(request,'core/Registro.html')
def Suspencion (request):
    return render(request,'core/Suspencion.html')