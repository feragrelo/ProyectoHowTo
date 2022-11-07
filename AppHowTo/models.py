import email
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, DateField, EmailField
from django.contrib.auth.models import User


    

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    fecha= models.DateField(null=True, blank=True)
    contenido=models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    respuesta=models.CharField(max_length=100)
    articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True, blank=True)