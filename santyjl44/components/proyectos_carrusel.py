import reflex as rx

from ..style import (
    proyecto_card_style, proyectos_carrusel_style,
    proyectos_carrusel_barra, boton_style, proyectos_style, Colors
    )


def proyectos_carrusel() -> rx.Component:
    imagenes = [
        rx.asset("proyectos/proyecto1.png"),
        rx.asset("proyectos/proyecto2.png"),
        rx.asset("proyectos/proyecto3.png")
    ]

    return rx.box(
        # ventana visible
        rx.text(
                "Proyectos",
                position="absolute",
                left=20,
                z_index=10,
                color=Colors.ACCENT.value
            ),
        rx.hstack(
            rx.heading("Algunos De Mis Trabajos", margin="25px",),
            rx.button(
                "Ver todos mis proyectos",
                style=boton_style,
                ),
            style=proyectos_carrusel_barra
            ),
            rx.hstack(

                *[
                    rx.image(
                        src=src,
                        style=proyectos_style
                    )
                    for src in imagenes * 2
                ],

                # fila que se mueve
                style=proyectos_carrusel_style
            ),
            style=proyecto_card_style
        ),

        