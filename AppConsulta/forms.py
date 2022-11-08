from django import forms
from django.contrib.auth.models import User
from AppConsulta.models import Consulta

class ConsultaFormulario(forms.Form):
    
    telefono=forms.IntegerField(label="Teléfono")
    email=forms.EmailField(label="Email")
    contenido= forms.CharField(label="Escriba su consulta:")
    
    class Meta:
        model = Consulta
        fields = ["telefono", "email", "contenido"]
    