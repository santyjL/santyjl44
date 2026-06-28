import reflex as rx

from ..style import navbar_style
from ..routers import ROUTES

def identificadores(nombre, id) -> rx.Component:
    return rx.box(
        rx.text(nombre),
        font_size="1em",
        font_weigth="bold",
        box_sizing="border-box",
        heigth="5px",
        padding="0.3em",
        color="#fff",
        cursor="pointer",
        _hover= {
            "border_bottom" : "3px solid #fff"
        },
        on_click=rx.redirect(path=id)
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
            rx.image(
                src=rx.asset("favicon.ico"),
                width="2.25em",
                height="auto",
                border_radius="25%",
            ),
            rx.heading("SANTYJL"),
            cursor="pointer",
            on_click=rx.redirect(path="/")
            ),
            
            rx.spacer(),
            identificadores("Inicio", "/"),
            identificadores("Sobre Mi", ROUTES["about"]),
            identificadores("proyectos", ROUTES["proyectos"]),
            identificadores("Servicios", ROUTES["services"]),
            identificadores("Contacto", ROUTES["contact"]),
        ),
        style=navbar_style,
    )
