from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import*

#http://127.0.0.1:8000/proyectoApp/

urlpatterns = [
    #url perfil: login logout register y editar perfil
    path('login/', login_request, name='login'),
    path('registro/', register, name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),

    #url noticias:
    path('noticias/', noticias.as_view(), name='noticias'),
    path('crearNoticias/', crear_noticias, name='crear_noticias'),
    path('leer_noticia/<id>', leer, name='leer'),
    

    #url comentarios:


]