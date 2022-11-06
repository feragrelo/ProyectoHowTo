from django import forms
from django.contrib.auth.models import User

class ConsultaFormulario(forms.Form):
    
    telefono=forms.IntegerField(label="Teléfono")
    email=forms.EmailField(label="Email")
    contenido= forms.CharField(label="Escriba su consulta:")
    
    class Meta:
        model = User
        fields = ["telefono", "email", "contenido"]
    