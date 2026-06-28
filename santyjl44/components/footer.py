import reflex as rx
from ..routers import ROUTES

from ..style import footer_style, Colors

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href, color=Colors.ACCENT.value)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("NAVEGACION", size="4", weight="bold", as_="h3"),
        footer_item("Inicio", "/#"),
        footer_item("Sobre Mi", ROUTES["about"]),
        footer_item("proyectos", ROUTES["proyectos"]),
        footer_item("Servicios", ROUTES["services"]),
        footer_item("Contacto", ROUTES["contact"]),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def social_link(label: str, href: str) -> rx.Component:
    return rx.link(rx.text(label, weight="bold"), href=href)

def socials() -> rx.Component:
    return rx.flex(
        social_link("IG", "/#"),
        social_link("YT", "/#"),
        social_link("META", "/#"),
        social_link("GITHUB", "/#"),
        spacing="3",
        justify="start",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src=rx.asset("favicon.ico"),
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading("SantyjL44", size="7", weight="bold"),
                        align_items="center",
                    ),
                    rx.text(
                        "Desarrollador Web Y Otras Cosas",
                        size="5",
                        white_space="nowrap",
                        weight="bold",
                    ),
                    rx.text(
                        "Creando experiencias digitales con amor y pasion.",
                        size="3",
                        white_space="wrap",
                        weight="medium",
                        text_wrap="pretty",
                        width="250px"
                    ),
                    spacing="4",
                    align_items=["center", "center", "start"],
                ),
                footer_items_1(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                socials(),
                rx.text(
                        "© 2026 SantyjL44",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        style=footer_style
    )