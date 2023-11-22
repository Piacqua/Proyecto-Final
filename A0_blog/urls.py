from django.urls import path
from A0_blog.views import (
    # LISTADO
    Boxeadores,
    Entrenadores,
    Arbitros,
    # FORMS
    Boxeadores_form,
    Entrenadores_form,
    Arbitros_form,
    # BUSQUEDA
    bbusqueda,
    ebusqueda,
    abusqueda,
    # EDITAR
    beditar,
    eeditar,
    aeditar,
    # BORRAR
    bborrar,
    eborrar,
    aborrar,
)

urlpatterns = [
    # ----------------------------------------------------------------------------------------
    # ----------
    # BOXEADOR
    # ----------
    path("boxeadores/", Boxeadores, name="lista_boxeadores"),  # LISTADO
    path(
        "registrarse-como-boxeador/", Boxeadores_form, name="registrarse_como_boxeador"
    ),  # FORM
    path("boxeadores/busqueda", bbusqueda, name="busqueda_boxeador"),  # BUSQUEDA
    path("editar-perfil-boxeador/<int:id>/", beditar, name="editar_boxeador"),  # EDITAR
    path(
        "borrar-perfil-boxeador/<int:id>/", bborrar, name="borrar_boxeador"
    ),  # ELIMINAR
    # ----------------------------------------------------------------------------------------
    # ----------
    # ENTRENADOR
    # ----------
    path("entrenadores/", Entrenadores, name="lista_entrenadores"),  # LISTADO
    path(
        "registrarse-como-entrenador/",
        Entrenadores_form,
        name="registrarse_como_entrenador",
    ),  # FORM
    path("entrenadores/busqueda", ebusqueda, name="busqueda_entrenador"),  # BUSQUEDA
    path(
        "editar-perfil-entrenador/<int:id>/", eeditar, name="editar_entrenador"
    ),  # EDITAR
    path(
        "borrar-perfil-entrenador/<int:id>/", eborrar, name="borrar_entrenador"
    ),  # ELIMINAR
    # ----------------------------------------------------------------------------------------
    # ----------
    # ARBITRO
    # ----------
    path("arbitros/", Arbitros, name="lista_arbitros"),  # LISTADO
    path(
        "registrarse-como-arbitro/",
        Arbitros_form,
        name="registrarse_como_arbitro",
    ),  # FORM
    path("arbitros/busqueda", abusqueda, name="busqueda_arbitro"),  # BUSQUEDA
    path("editar-perfil-arbitro/<int:id>/", aeditar, name="editar_arbitro"),  # EDITAR
    path("borrar-perfil-arbitro/<int:id>/", aborrar, name="borrar_arbitro"),  # ELIMINAR
]
