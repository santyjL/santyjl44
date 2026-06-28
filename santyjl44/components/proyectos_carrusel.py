import reflex as rx

from ..states.lista_proyectos import proyectos
from ..style import (
    proyecto_card_style, proyectos_carrusel_style,
    proyectos_carrusel_barra, boton_style, proyectos_style,
    proyecto_modal, titulo_modal,imagen_proyecto_modal,
    Colors,botones_modal
    )


def proyecto(src: str, titulo: str, descripcion: str,url:str ) -> rx.Component:

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.image(
                src=src,
                style=proyectos_style,
                cursor="pointer",
            )
        ),
        rx.dialog.content(
            rx.dialog.title(
                titulo,
                style=titulo_modal
            ),
            rx.image(
                src=src,
                style=imagen_proyecto_modal
                ),
                
                rx.dialog.description(
                    descripcion,
                    margin="10px"
                ),
                rx.hstack(
                    rx.dialog.close(
                        rx.button(
                            "⬅ volver",
                            style=boton_style
                        ),
                    ),
                    rx.button(
                        "Explora Proyecto ➡", 
                        style=boton_style,
                        on_click=rx.redirect(url, is_external=True)
                    ),
                    style=botones_modal
                ),
            style=proyecto_modal 
        ),
    )
    
def proyectos_carrusel() -> rx.Component:
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
            style=proyectos_carrusel_barra
            ),
        rx.hstack(
            *[
            proyecto(
                    p["src"],
                    p["titulo"],
                    p["descripcion"],
                    p["url"]
                )
                for p in proyectos * 3
            ],
            # fila que se mueve
            style=proyectos_carrusel_style
        ),
        style=proyecto_card_style,
        id="proyectos"
    )
        