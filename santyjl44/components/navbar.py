import reflex as rx

from ..style import navbar_style, Font, Colors
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

def navbar_movil () -> rx.Component:
    return rx.mobile_only(
        rx.drawer.root(
            rx.drawer.trigger(
                rx.icon_button(
                    "menu",
                    variant="ghost",
                    color="white",
                )
            ),

            rx.drawer.overlay(),

            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        rx.drawer.close(
                            identificadores("Inicio", "/"),
                        ),
                        rx.drawer.close(
                            identificadores("Sobre Mi", ROUTES["about"]),
                        ),
                        rx.drawer.close(
                            identificadores("Proyectos", ROUTES["proyectos"]),
                        ),
                        rx.drawer.close(
                            identificadores("Servicios", ROUTES["services"]),
                        ),rx.drawer.close(
                            identificadores("Contacto", ROUTES["contact"]),
                        ),

                        spacing="4",
                        width="100%",
                        align="start",
                        padding="2rem",
                    ),
                    bg=Colors.COFFEE_DARK.value,
                    border_left=f"3px solid {Colors.DESTACAR.value}",
                )
            ),
            direction="right",
        )
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
            rx.heading("SANTYJL", font_family=Font.HANDWRITING.value,),
            cursor="pointer",
            on_click=rx.redirect(path="/")
            ),
            
            rx.spacer(),
            rx.desktop_only(
                rx.hstack(
                    identificadores("Inicio", "/"),
                    identificadores("Sobre Mi", ROUTES["about"]),
                    identificadores("Proyectos", ROUTES["proyectos"]),
                    identificadores("Servicios", ROUTES["services"]),
                    identificadores("Contacto", ROUTES["contact"]),
                    spacing="5",
                )
            ),
            rx.mobile_only(
                navbar_movil()
            ),
        ),
        style=navbar_style,
    )
