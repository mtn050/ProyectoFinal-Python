from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class Registro(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {campo:"" for campo in fields}

class Edicion(UserCreationForm):
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class Opiniones_form(forms.Form):
    opinion=forms.CharField(max_length=150)

class Noticias_form(forms.Form):
    Titulo=forms.CharField(max_length=50)
    Subtitulo=forms.CharField(max_length=50)
    Cuerpo=forms.CharField(max_length=500)