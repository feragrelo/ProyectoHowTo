from django.urls import path

from AppConsulta.views import(ConsultaCreacion)

urlpatterns = [
    path("consulta/", ConsultaCreacion.as_view(), name="ConsultaNueva"),
    
]