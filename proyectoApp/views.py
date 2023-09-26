from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import Registro, Edicion, Opiniones_form, Noticias_form
from .models import Noticias
from django.contrib.auth.forms import   AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.

def inicio (request):
    return render ( request, 'inicio.html')


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Bienvenido {usu}"})
            else:
                return render(request,"login.html", {"form":form})
        else:
            return render(request,"login.html", {"form":form})
    else:
        form=AuthenticationForm()
        return render(request,"login.html", {"form":form})

def register(request):
    if request.method=="POST":
        form=Registro(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente"})
        else:
            return render(request,"register.html", {"form":form, "mensaje":"Datos invalidos"})

    else:
        form=Registro()
        return render(request,"register.html", {"form":form})
    
@login_required
def editarPerfil(request):
    usuario=request.user
    
    if request.method=="POST":
        form=Edicion(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        form=Edicion(instance=usuario)
        return render(request, "editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

def buscar(request):
    return render ( request, 'inicio.html')

def comentarios(request):
     #usuario=request.user
   
    if request.method=="POST":
        form=Opiniones_form(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            opinion=info["opinion"]
            opiniones.save()
            return render(request,"opinion.html")
        return render(request,"AppCoder/cursos.html", {"mensaje":"Datos invalidos"})
    else:
        formulario=Opiniones_form()
        return render(request,"opinion.html")
   
def crear_comentarios(request):
    return render ( request, 'inicio.html')

def borrar_comentarios(request):
    return render ( request, 'inicio.html')



   
class noticias(ListView):
    def get(self,request):
        noticias=Noticias.objects.all()
        template_name= "noticias.html"
        return render(request, template_name, {"noticias": noticias})
    
def leer(request, id):
    noticia=Noticias.objects.get(id=id)
    return render (request, 'leer.html', {"noticia": noticia})    
    

        
def crear_noticias(request):
    if request.method=="POST":
        form=Noticias_form(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            titulo=info["Titulo"]
            subtitulo=info["Subtitulo"]
            cuerpo=info["Cuerpo"]
            noticia=Noticias(Titulo=titulo,Subtitulo=subtitulo,Cuerpo=cuerpo)
            noticia.save()
            return render(request,"noticias.html", {"mensaje":"Noticia creada", "noticia":noticia})
        else:
            return render(request,"crearNoticia.html",  {"formulario":form})
    else:
        form=Noticias_form()
        return render(request,"crearNoticia.html", {"formulario":form})


def borrar_noticias(request):
    return render ( request, 'inicio.html')

def borrar_noticias(request):
    return render ( request, 'inicio.html')
