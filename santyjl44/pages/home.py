import reflex as rx

from ..components.navbar import navbar
from ..components.hero import hero
from ..components.footer import footer
from ..components.proyectos_carrusel import proyectos_carrusel
from ..style import sobre_mi_style, foto_sobre_mi_style, boton_style, body, fondo

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

def home() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            hero(),
            sobre_mi(),
            proyectos_carrusel(),
            footer(),
            style=body
        ),
        style=fondo
    )
