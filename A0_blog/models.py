from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Arbitro(models.Model):
    class EXPERIENCIA(models.TextChoices):
        MENOR5 = "Menor a 5 años", "Menor a 5 años"
        MAYOR5 = "Mayor a 5 años", "Mayor a 5 años"
        MAYOR10 = "Mayor a 10 años", "Mayor a 10 años"

    nombre = models.CharField(max_length=64, blank=False)
    edad = models.IntegerField()
    experiencia = models.CharField(
        max_length=16, blank=False, choices=EXPERIENCIA.choices
    )
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.experiencia}"


class Boxeador(models.Model):
    class CATEGORIAS(models.TextChoices):
        INFANTIL = "Infantil", "Infantil"
        ADOLESCENCIA = "Adolescencia", "Adolescencia"
        PLUMA = "Pluma", "Pluma"
        LIGERO = "Ligero", "Ligero"
        SEMIPESADO = "Semi-Pesado", "Semi-Pesado"
        PESADO = "Pesado", "Pesado"

    class EDADES(models.TextChoices):
        E5_12 = "5 a 12 años", "5 a 12 años"
        E13_17 = "13 a 17 años", "13 a 17 años"
        E18 = "Mayor de edad", "Mayor de edad"

    nombre = models.CharField(max_length=64, blank=False)
    peso = models.CharField(max_length=16, choices=CATEGORIAS.choices, blank=False)
    edad = models.CharField(max_length=16, blank=False, choices=EDADES.choices)
    peleas = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.peso}, {self.peleas}, {self.victorias}, {self.derrotas} "


class Entrenador(models.Model):
    class EXPERIENCIA(models.TextChoices):
        MENOR5 = "Menor a 5 años", "Menor a 5 años"
        MAYOR5 = "Mayor a 5 años", "Mayor a 5 años"
        MAYOR10 = "Mayor a 10 años", "Mayor a 10 años"

    nombre = models.CharField(max_length=64)
    edad = models.IntegerField()
    experiencia = models.CharField(
        max_length=16, blank=False, choices=EXPERIENCIA.choices
    )
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.experiencia}"
