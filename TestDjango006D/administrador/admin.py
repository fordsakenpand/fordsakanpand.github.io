from django.contrib import admin
from .models import Administrador,Categoria,Vehiculo

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Categoria)
admin.site.register(Vehiculo)