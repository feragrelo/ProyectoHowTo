import email
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, DateField, EmailField
from django.contrib.auth.models import User

class Autor (models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    
    def __str__(self):
        return f" {self.nombre}"
    

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    contenido=models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    respuesta=models.CharField(max_length=100)
    articulo=models.ForeignKey(Articulo, on_delete=models.CASCADE)
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True, blank=True)