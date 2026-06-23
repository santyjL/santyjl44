import reflex as rx

from ..style import hero_style


def hero() -> rx.Component:
    return rx.box(
        rx.box(padding="4.5em 0px"),
        rx.heading("Bienvenido", font_size="5em"),
        style=hero_style,
    )
