from django.db import models

class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True,verbose_name="id de categoria")
    nombrecategoria = models.CharField(max_length=50,verbose_name="nombre de categoria")
    def __str__(self):
        return self.nombrecategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True,max_length=6, verbose_name="patente") 
    maraca = models.CharField(max_length=20,verbose_name="maraca vehiculo")
    modelo = models.CharField(max_length=20,null=True,blank=True,verbose_name="modelo")
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)  

    def __str__(self):
        return self.patente
 

