import reflex as rx

from ..states.logic import StateYoutube
from ..style import (
    sobre_mi_style, foto_sobre_mi_style,
    boton_style, sobre_mi_seccion_style,
    foto_datos_style
)

def datos_canal(icon_tag, estado) -> rx.Component:
    return rx.hstack(
        rx.icon(
            tag=icon_tag,
            width="48px",
            height="48px"
        ),
        rx.text(
            estado,
            font_size="2em",
            weight="bold"
        ),
        position="relative",
        transition= "all .7s",
        _hover={
            "top" : "-10px",
            "scale" : "1.03"
        }
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
        rx.box(
            datos_canal("users-round", StateYoutube.subscribers),
            datos_canal("eye", StateYoutube.total_views),
            datos_canal("tv-minimal-play", StateYoutube.total_videos),
            style=foto_datos_style
        ),
        style=sobre_mi_seccion_style
        
    )
