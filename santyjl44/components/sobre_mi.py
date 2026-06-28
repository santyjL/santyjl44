import reflex as rx

from ..states.logic import StateYoutube
from ..style import (
    sobre_mi_style, foto_sobre_mi_style,
    boton_style, sobre_mi_seccion_style,
    foto_datos_style, Colors, Font
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
            "top" : "-5px",
            "scale" : "1.03"
        }
    )

def sobre_mi () -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "Sobre mi",
                position="absolute",
                top=140,
                left=20,
                color=Colors.ACCENT.value
            ),
            rx.heading(
                "Construyendo Ideas Que Dejan Huella",
                margin="20px 0",
                size="8",
                font_family=Font.TITLE.value
            ),
            rx.text(
            """Apasionado por el desarrollo web y el diseño, me especializo en
            crear experiencias digitales que no solo se ven bien, sino que funcionan
            perfecto. Cada proyecto es una oportunidad para transformar ideas 
            en soluciones reales."""
            ),
            rx.button(
                "Contactame",
                style=boton_style,
                on_click=rx.redirect("https://youtube.com")
            ),
            align_items="left",
            style=sobre_mi_style
        ),
        rx.box(
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
            rx.button(
                "Mira el video de presentacion",
                position="relative",
                left="32%",
                style=boton_style,
            ),
        ),
        style=sobre_mi_seccion_style,
        id="sobre-mi"
    )
