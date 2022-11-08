from django.urls import path
from django.contrib.auth.views import LogoutView
from AppHowTo.views import(inicio,MyLogin,ListaArticulos,ArticuloCreacion,
registrarse,editar_perfil, agregar_avatar,ArticuloDetalle,ArticuloDelete,ArticuloUpdateView,about_us,ComentarioCreacion)

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('about_us/', about_us, name="About_us"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("articulo/list", ListaArticulos.as_view(), name="ListaArticulos"),
    path("articulo-nuevo/", ArticuloCreacion.as_view(), name="ArticuloNuevo"),
    path("registrarse/", registrarse, name="Registrarse"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
    path("logout/",LogoutView.as_view(template_name="AppHowto/logout.html"),name="Logout"),
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
    path("curso/<pk>'", ArticuloDetalle.as_view(), name="ArticuloDetail"),
    path("editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
    path("borrar/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    path("", inicio),
    #path('hacer_comentario/', hacer_comentario, name="HacerComentario"),
    path("comentario/<pk>", ComentarioCreacion.as_view(), name="ComentarioNuevo"),
]