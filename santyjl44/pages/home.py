import reflex as rx

from ..components.navbar import navbar
from ..components.hero import hero
from ..components.footer import footer
from ..components.proyectos_carrusel import proyectos_carrusel
from ..style import (
    sobre_mi_style, foto_sobre_mi_style,
    boton_style, body, fondo,
    servicios_style, youtube_style, skills_style
    )

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
        display="flex",
        flex_flow="row nowrap",
        columns=2,
        margin=0
        
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
            gap="40px",
            justify_content="center",
            padding="1em",
        )
    )

def home() -> rx.Component:
    return rx.center(
        navbar(),
        rx.box(
            hero(),
            sobre_mi(),
            proyectos_carrusel(),
            me_diferencia(),
            footer(),
            style=body
        ),
        style=fondo
    )
