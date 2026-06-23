import reflex as rx

from ..style import (
    proyecto_card_style, proyectos_carrusel_style,
    proyectos_carrusel_barra, boton_style
    )


def proyectos_carrusel() -> rx.Component:
    imagenes = [
        "/placeholder.png",
        "/placeholder.png",
        "/placeholder.png",
    ]

    return rx.box(

        # ventana visible
        rx.hstack(
            rx.vstack(
                rx.heading("proyectos"),
                rx.button(
                    "Mira mas proyectos",
                    style=boton_style
                    ),
                style=proyectos_carrusel_barra
            ),
            rx.hstack(

                *[
                    rx.image(
                        src=src,
                        width="400px",
                        height="250px",
                        object_fit="cover",
                        flex_shrink="0",
                    )
                    for src in imagenes * 2
                ],

                # fila que se mueve
                style=proyectos_carrusel_style

            ),
        ),

        style=proyecto_card_style
    )