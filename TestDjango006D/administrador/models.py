from django.db import models
 
# Create your models here.
class Administrador(models.Model):
        useradmin = models.CharField(max_length=50,verbose_name="Nombre de usuario")
        contra = models.CharField(primary_key=True,max_length=10,verbose_name="Contraseña")
    def __str__(self):
        return self.useradmin