from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import*

#http://127.0.0.1:8000/proyectoApp/

urlpatterns = [
    path('login/', login_request, name='login'),
    path('registro/', register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),


    path('noticias/', noticias.as_view(), name='noticias'),

    path('crearNoticias/', crear_noticias, name='crear_noticias'),


]