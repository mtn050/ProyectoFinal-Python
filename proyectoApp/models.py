from django.db import models

# Create your models here.

class Noticias(models.Model):
    Titulo=models.CharField(max_length=500)
    Subtitulo=models.CharField(max_length=500)
    Cuerpo=models.CharField(max_length=1500)
    def __str__(self):
        return f"{self.Titulo}"

class Opiniones(models.Model):
    Quien=models.CharField(max_length=50)
    opinion=models.CharField(max_length=150)
