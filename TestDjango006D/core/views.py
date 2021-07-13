from django.shortcuts import render

# Create your views here.
def Cambios (request):
    return render(request,'core/Cambios.html')
def Contacto (request):
    return render(request,'core/Contacto.html')
def Electricidad (request):
    return render(request,'core/Electricidad.html')

class titu:
    def __init__(self,electro,caja,suspen):
        self.electro=electro
        self.caja=caja
        self.suspen=suspen
        super().__init__()
def Index (request):

    titulo=titu("Especialista en electricidad","Especialista en caja de cambios","Especialista en suspencion")
    descrip=["Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, asperiores laboriosam eum incidunt consectetur, debitis cupiditate doloremque quibusdam fugiat nisi dolore facere distinctio accusantium quia, eligendi quas? In, corporis molestiae.",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptates dolore neque quaerat ratione obcaecati illo deleniti unde harum! Neque sint, qui ducimus officiis pariatur commodi veritatis? Deserunt non aut suscipit.",
             "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Velit corrupti fuga adipisci sit voluptatum recusandae iste eos odio eligendi quia nobis explicabo vitae accusamus saepe, culpa sed magni quidem animi!"]
    contexto={"titulo":titulo,"texto":descrip}

    return render(request,'core/Index.html',contexto)
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