import email
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from AppHowTo.models import Autor,Articulo,Comentario,Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from AppHowTo.forms import AvatarForm, UserEditionForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class ListaArticulos(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = "AppHowto/lista_articulos.html"
    
@login_required
def listar_articulos(request):
    articulos = Articulo.objects.all()
    avatar = Avatar.objects.filter(user=request.user).first()
    contexto = {
        "articulos_encontrados": articulos,
        "avatar": avatar.imagen.url
    }

    return render(request, "AppHowto/listar-articulos.html", contexto)  

class ArticuloDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = "AppHowto/articulo_detalle.html"


class ArticuloCreacion(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ["nombre", "contenido","autor"]
    success_url = "/AppHowto/articulo/list"


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = "/AppHowto/articulo/list"
    fields = ["nombre", "contenido","autor"]


class ArticuloDelete(LoginRequiredMixin, DeleteView):

    model = Articulo
    success_url = "/AppHowto/articulo/list"
#..........................................................

class MyLogin(LoginView):
    template_name = "AppHowto/login.html"
    

@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request,"AppHowto/inicio.html", contexto)

@login_required
def about_us(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request,"AppHowto/about_us.html", contexto)


def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "AppHowto/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "AppHowto/registrarse.html", {"form": form})


@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "AppHowto/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {
        "user": user,
        "form": form,
        "avatar": avatar.imagen.url
    }
    return render(request, "AppHowto/editar_perfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            
            return render(request, "AppHowto/inicio.html")

    contexto = {"form": form}   
    return render(request, "AppHowto/avatar_form.html", contexto)
