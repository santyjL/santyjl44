import reflex as rx

from ..style import contacto_style, boton_style, Colors, Font

def contacto() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.box(
                rx.icon(
                    tag="rocket",
                    width="48px",
                    height="48px",
                    color=Colors.COFFEE.value,
                ),
                bg=Colors.PAPER.value,
                padding="0.5em",
                border_radius="50%"
            ),
            rx.vstack(
                rx.heading(
                    "¿Tienes Un Proyecto En Mente?",
                    font_size="1.8em",
                    font_family=Font.TITLE.value
                    ),
                rx.text(
                    "Estoy listo para ayudarte a hacerlo realidad",
                    position="relative",
                    top="-10px",
                    opacity=0.7
                )
            ),
            rx.button(
                "Contactame ➡",
                style=boton_style
            )
        ),
        style=contacto_style,
        id="contacto"
    )