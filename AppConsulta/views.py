from django.shortcuts import render
from AppConsulta.forms import ConsultaFormulario
from AppConsulta.models import Consulta

def hacer_consulta(request):
    if request.method != "POST":
        formulario = ConsultaFormulario()
    else:
        formulario = ConsultaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            consulta = Consulta(telefono=informacion["telefono"], email=informacion["email"],contenido=informacion["contenido"])
            consulta.save()
            return render(request, "AppHowTo/inicio.html")

    contexto = {"formulario_consulta": formulario}

    return render(request, "AppConsulta/formulario_consulta.html", contexto)