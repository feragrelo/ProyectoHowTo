from django.db import models
from django.forms import CharField, IntegerField, EmailField
from django.contrib.auth.models import User

class Consulta (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    contenido=models.CharField(max_length=3000,null=True, blank=True)
    telefono=models.IntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.contenido
    
    