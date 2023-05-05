from django.db import models

# Create your models here.


class Ciudad(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)


class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    fechaNacimiento = models.DateField()
    ciudad = models.ForeignKey(
        Ciudad, blank=False, null=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt = "{0}{1}"
        return txt.format(self.apellido, self.nombre)


class Telefono(models.Model):
    persona = models.ForeignKey(
        Persona, blank=False, null=False, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)


class Email(models.Model):
    persona = models.ForeignKey(
        Persona, blank=False, null=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=180)
