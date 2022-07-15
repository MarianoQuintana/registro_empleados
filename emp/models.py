from django.db import models

class Datos_personales(models.Model):    
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=3)
    domicilio = models.TextField(max_length=255)
    tel = models.IntegerField(20)
    email = models.EmailField()

