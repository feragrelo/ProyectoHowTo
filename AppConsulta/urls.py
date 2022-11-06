from django.urls import path

from AppConsulta.views import(hacer_consulta)

urlpatterns = [
    path('hacer_consulta/', hacer_consulta, name="Hacer consulta"),
    
]