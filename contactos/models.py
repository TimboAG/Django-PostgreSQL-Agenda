from django.db import models

# Create your models here.


class Ciudad(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)


class Persona(models.Model):
    dni = models.PositiveSmallIntegerField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
