import reflex as rx

from ..style import (
    Colors,servicios_style,
    youtube_style, skills_style,
    me_diferencia_style,
    )

def titulo_card_trabajo(icon, titulo, subtitulo):
    return rx.hstack(
        rx.box(
            rx.icon(
                tag=icon,
                width="32px",
                height="32px",
                color=Colors.COFFEE.value,
            ),
            bg=Colors.PAPER_DARK.value,
            padding="0.5em",
            border_radius="50%"
        ),
        rx.vstack(
            rx.heading(titulo),
            rx.text(subtitulo, position="relative", top="-10px")
        ),
        margin_bottom="20px",
        border_bottom="1px solid #111",
    )


def me_diferencia () -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                titulo_card_trabajo(
                    "shopping-bag",
                    "Servicios Que Ofrezco",
                    "Soluciones digitales a medida"
                ),
                rx.unordered_list(
                    rx.list_item( "Crear landing Page",),
                    rx.list_item( "Crear Porfolios",),
                    rx.list_item( "Crear LinksBios Personalizadas"),    
                ),
                style=servicios_style
            ),
            rx.box(
                titulo_card_trabajo(
                    "rocket",
                    "Mi Proceso De Trabajo",
                    "Simple, claro y efectivo"
                ),
            style=youtube_style
            ),
            rx.box(
                titulo_card_trabajo(
                    "code-xml",
                    "Tecnologias Que Uso",
                    "Herramientas para crear soluciones"
                ),
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
        ), 
    )
