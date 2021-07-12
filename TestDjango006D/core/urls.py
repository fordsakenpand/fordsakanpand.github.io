from django.urls import path 
from .views import Cambios
from .views import Contacto
from .views import Electricidad
from .views import Index
from .views import MecaCam
from .views import MecaEle
from .views import MecaSus
from .views import Registro
from .views import Suspencion

urlpatterns = [
    path ('Cambios.html',Cambios,name="Cambios"),
    path ('Contacto.html',Contacto,name="Contacto"),
    path ('Electricidad.html',Electricidad,name="Electricidad"),
    path ('Index.html',Index,name="Index"),
    path ('',Index,name="Index"),
    path ('MecaCam.html',MecaCam,name="MecaCam"),
    path ('MecaEle.html',MecaEle,name="MecaEle"),
    path ('MecaSus.html',MecaSus,name="MecaSus"),
    path ('Registro.html',Registro,name="Registro"),
    path ('Suspencion.html',Suspencion,name="Suspencion")
]