import reflex as rx

from ..style import contacto_style, boton_style

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
