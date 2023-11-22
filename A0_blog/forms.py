from django import forms
from A0_blog.models import Boxeador, Arbitro, Entrenador


class Arbitro_Formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    edad = forms.IntegerField(required=True, min_value=18, max_value=99)
    experiencia = forms.ChoiceField(required=True, choices=Arbitro.EXPERIENCIA.choices)


class Boxeador_Formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    peso = forms.ChoiceField(required=True, choices=Boxeador.CATEGORIAS.choices)
    edad = forms.ChoiceField(required=True, choices=Boxeador.EDADES.choices)


class Entrenador_Formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    edad = forms.IntegerField(required=True, min_value=18, max_value=99)
    experiencia = forms.ChoiceField(
        required=True, choices=Entrenador.EXPERIENCIA.choices
    )
