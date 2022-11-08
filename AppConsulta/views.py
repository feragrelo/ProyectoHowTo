from django.shortcuts import render
from AppConsulta.models import Consulta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


class ConsultaCreacion(LoginRequiredMixin, CreateView):
    model = Consulta
    fields = ["user","contenido","telefono","email"]
    success_url = "/AppHowto/inicio"
    
