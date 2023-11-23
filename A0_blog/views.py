from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from A0_blog.forms import Arbitro_Formulario, Boxeador_Formulario, Entrenador_Formulario
from A0_blog.models import Boxeador, Entrenador, Arbitro


# Create your views here.
# LISTADO
#
# ------------------------
def Boxeadores(request):
    contexto = {"total": Boxeador.objects.all()}
    http_response = render(
        template_name="boxeadores.html", request=request, context=contexto
    )
    return http_response


def Entrenadores(request):
    contexto = {"total": Entrenador.objects.all()}
    http_response = render(
        template_name="entrenadores.html", request=request, context=contexto
    )
    return http_response


def Arbitros(request):
    contexto = {"total": Arbitro.objects.all()}
    http_response = render(
        template_name="arbitros.html", request=request, context=contexto
    )
    return http_response


# FORMS
#
# ------------------------
@login_required
def Boxeadores_form(request):
    user = request.user

    if request.method == "POST":
        formulario = Boxeador_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            peso = data["peso"]
            edad = data["edad"]

            boxeador = Boxeador(
                nombre=nombre, edad=edad, peso=peso, creador=request.user
            )
            boxeador.save()

            url_exitosa = reverse("lista_boxeadores")
            return redirect(url_exitosa)
    else:  # GET
        formulario = Boxeador_Formulario(
            initial={"nombre": f"{user.first_name} {user.last_name}"}
        )
    http_response = render(
        request=request,
        template_name="form_boxeador.html",
        context={"formulario": formulario},
    )
    return http_response


@login_required
def Entrenadores_form(request):
    user = request.user

    if request.method == "POST":
        formulario = Entrenador_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            experiencia = data["experiencia"]
            edad = data["edad"]

            entrenador = Entrenador(
                nombre=nombre, edad=edad, experiencia=experiencia, creador=request.user
            )
            entrenador.save()

            url_exitosa = reverse("lista_entrenadores")
            return redirect(url_exitosa)
    else:  # GET
        formulario = Entrenador_Formulario(
            initial={"nombre": f"{user.first_name} {user.last_name}"}
        )
    http_response = render(
        request=request,
        template_name="form_entrenador.html",
        context={"formulario": formulario},
    )
    return http_response


@login_required
def Arbitros_form(request):
    user = request.user

    if request.method == "POST":
        formulario = Arbitro_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            experiencia = data["experiencia"]
            edad = data["edad"]

            arbitro = Arbitro(
                nombre=nombre, edad=edad, experiencia=experiencia, creador=request.user
            )
            arbitro.save()

            url_exitosa = reverse("lista_arbitros")
            return redirect(url_exitosa)
    else:  # GET
        formulario = Arbitro_Formulario(
            initial={"nombre": f"{user.first_name} {user.last_name}"}
        )
    http_response = render(
        request=request,
        template_name="form_arbitro.html",
        context={"formulario": formulario},
    )
    return http_response


# BUSQUEDAS
#
# ------------------------
def bbusqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        bboxeador = Boxeador.objects.filter(
            Q(nombre__icontains=busqueda)
            | Q(edad__icontains=busqueda)
            | Q(peso__icontains=busqueda)
            | Q(peleas__icontains=busqueda)
            | Q(victorias__icontains=busqueda)
            | Q(derrotas__icontains=busqueda)
        )

        contexto = {
            "total": bboxeador,
        }
        http_response = render(
            request=request,
            template_name="boxeadores.html",
            context=contexto,
        )
        return http_response


def ebusqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        bentrenador = Entrenador.objects.filter(
            Q(nombre__icontains=busqueda)
            | Q(edad__icontains=busqueda)
            | Q(experiencia__icontains=busqueda)
        )

        contexto = {
            "total": bentrenador,
        }
        http_response = render(
            request=request,
            template_name="entrenadores.html",
            context=contexto,
        )
        return http_response


def abusqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        barbitro = Arbitro.objects.filter(
            Q(nombre__icontains=busqueda)
            | Q(edad__icontains=busqueda)
            | Q(experiencia__icontains=busqueda)
        )

        contexto = {
            "total": barbitro,
        }
        http_response = render(
            request=request,
            template_name="arbitros.html",
            context=contexto,
        )
        return http_response


# EDITAR
#
# ------------------------
@login_required
def beditar(request, id):
    boxeador = Boxeador.objects.get(id=id)

    if request.method == "POST":
        formulario = Boxeador_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            boxeador.nombre = data["nombre"]
            boxeador.edad = data["edad"]
            boxeador.peso = data["peso"]
            boxeador.save()

            url_exitosa = reverse("lista_boxeadores")
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            "nombre": boxeador.nombre,
            "edad": boxeador.edad,
            "peso": boxeador.peso,
        }
        formulario = Boxeador_Formulario(initial=inicial)
    http_response = render(
        request=request,
        template_name="form_boxeador.html",
        context={"formulario": formulario},
    )
    return http_response


@login_required
def eeditar(request, id):
    entrenador = Entrenador.objects.get(id=id)

    if request.method == "POST":
        formulario = Entrenador_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            entrenador.nombre = data["nombre"]
            entrenador.edad = data["edad"]
            entrenador.experiencia = data["experiencia"]
            entrenador.save()

            url_exitosa = reverse("lista_entrenadores")
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            "nombre": entrenador.nombre,
            "edad": entrenador.edad,
            "experiencia": entrenador.experiencia,
        }
        formulario = Entrenador_Formulario(initial=inicial)
    http_response = render(
        request=request,
        template_name="form_entrenador.html",
        context={"formulario": formulario},
    )
    return http_response


@login_required
def aeditar(request, id):
    arbitro = Arbitro.objects.get(id=id)

    if request.method == "POST":
        formulario = Arbitro_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            arbitro.nombre = data["nombre"]
            arbitro.edad = data["edad"]
            arbitro.experiencia = data["experiencia"]
            arbitro.save()

            url_exitosa = reverse("lista_arbitros")
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            "nombre": arbitro.nombre,
            "edad": arbitro.edad,
            "experiencia": arbitro.experiencia,
        }
        formulario = Arbitro_Formulario(initial=inicial)
    http_response = render(
        request=request,
        template_name="form_arbitro.html",
        context={"formulario": formulario},
    )
    return http_response


# BORRAR
#
# ------------------------
@login_required
def bborrar(request, id):
    boxeador = Boxeador.objects.get(id=id)
    if request.method == "POST":
        boxeador.delete()
        url_exitosa = reverse("lista_boxeadores")
        return redirect(url_exitosa)


@login_required
def eborrar(request, id):
    entrenador = Entrenador.objects.get(id=id)
    if request.method == "POST":
        entrenador.delete()
        url_exitosa = reverse("lista_entrenadores")
        return redirect(url_exitosa)


@login_required
def aborrar(request, id):
    arbitro = Arbitro.objects.get(id=id)
    if request.method == "POST":
        arbitro.delete()
        url_exitosa = reverse("lista_arbitros")
        return redirect(url_exitosa)
