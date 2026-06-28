import reflex as rx

from ..states.logic import StateYoutube
from ..components.contacto import boton_contacto
from ..style import (
    sobre_mi_style, foto_sobre_mi_style,
    boton_style, sobre_mi_seccion_style,
    foto_datos_style, Colors, Font
)

YOUTUBE_PRESENTACION = "https://www.youtube.com/embed/sNUA8qe5aoc"

def modal_presentacion() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Mira el video de presentación",
                position="relative",
                left="32%",
                style=boton_style,
            )
        ),

        rx.dialog.content(

            rx.el.iframe(
                src=YOUTUBE_PRESENTACION,
                width="100%",
                height="500px",
                allow=(
                    "accelerometer; autoplay; "
                    "clipboard-write; encrypted-media; "
                    "gyroscope; picture-in-picture"
                ),
                allow_full_screen=True,
                border="none",
                border_radius="10px",
            ),

            rx.dialog.close(
                rx.icon_button(
                    "x",
                    position="absolute",
                    top="15px",
                    right="15px",
                    bg=Colors.ACCENT.value,
                )
            ),

            background=Colors.COFFEE_BLACK.value,
            padding="1rem",
            max_width="900px",
            width="90vw",
            border=f"1px solid {Colors.LINEAS.value}",
            border_top=f"5px solid {Colors.DESTACAR.value}",
            border_radius="20px",
        ),
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
        top=0,
        transition= "all .7s .1s",
        _hover={
            "top" : "-5px",
            "scale" : "1.05"
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
            boton_contacto(),
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
            modal_presentacion(),
        ),
        style=sobre_mi_seccion_style,
        id="sobre-mi"
    )
