import reflex as rx

from ..components.navbar import navbar
from ..components.hero import hero
from ..components.footer import footer
from ..components.proyectos_carrusel import proyectos_carrusel
from ..style import (
    contacto_style, sobre_mi_style, foto_sobre_mi_style,
    boton_style, body, fondo,
    servicios_style, youtube_style, skills_style,
    me_diferencia_style, sobre_mi_seccion_style
    )
from ..states.logic import StateYoutube

def sobre_mi () -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading(
                "Sobre Mi",
                margin="20px 0"
                ),
            rx.text(
            """mucho texto para rellenar la pagina y no se mire vacia porque si no no me sirve y
            asi entonces extiendo mas el texto hasta que me de para todo un testamente donde heredo
            los unicos 2 gatos que poseo porque son lo mas preciado para mi"""
            ),
            rx.vstack(
                rx.button(
                    "Conoceme mejor",
                    style=boton_style,
                    on_click=rx.redirect("https://youtube.com")
                ),
                rx.button(
                    "Contactame",
                    style=boton_style,
                    on_click=rx.redirect("https://youtube.com")
                ),
                align_items="center"
            ),
            style=sobre_mi_style
        ),
        rx.image(
            src=rx.asset("sobre_mi.png"),
            style=foto_sobre_mi_style
        ),
        style=sobre_mi_seccion_style
        
    )

def me_diferencia () -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                rx.heading("Servicios"),
                rx.unordered_list(
                    rx.list_item( "Crear landing Page",),
                    rx.list_item( "Crear Porfolios",),
                    rx.list_item( "Crear LinksBios Personalizadas"),
                ),
                style=servicios_style
            ),
            rx.box(
                rx.heading("Mi Canal De Youtube"),
                rx.text(f"nombre: {StateYoutube.nombre_canal}"),
                rx.text(f"Subscritores: {StateYoutube.subscribers}"),
                rx.text(f"Vistas: {StateYoutube.total_views}"),
                rx.text(f"videos: {StateYoutube.total_videos} "),
                rx.video(
                    src="https://www.youtube.com/watch?v=H7hDPqcUKhk"
                ),
                style=youtube_style
            ),
            rx.box(
                rx.heading("Skills"),
                rx.unordered_list(
                    rx.list_item( "Python",),
                    rx.list_item( "Reflex"),
                    rx.list_item( "Git",),
                    rx.list_item( "GitHub"),
                    rx.list_item( "Css",),
                    rx.list_item( "HTML",),
                    rx.list_item( "Cursor"),
                    rx.list_item( "Diseño Responsivo"),
                    justify_items="start",
                ),
                style=skills_style
            ),
            
            style=me_diferencia_style
        )
    )

def contacto() -> rx.Component:
    return rx.box(
        rx.center(
            rx.text(
                "si ves que puedo darte la solucion que buscas no lo dudes."
            ),
            rx.button(
                "Contactame",
                style=boton_style,
                on_click=rx.redirect("https://youtube.com" , is_external=True)
            ),
            display="flex",
            flex_direction="column",
        ),
        style=contacto_style
    )

def home() -> rx.Component:
    return rx.center(
        navbar(),
        rx.box(
            hero(),
            sobre_mi(),
            proyectos_carrusel(),
            me_diferencia(),
            contacto(),
            footer(),
            style=body
        ),
        style=fondo
    )
