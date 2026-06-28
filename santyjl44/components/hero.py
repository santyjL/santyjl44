from turtle import right
import reflex as rx

from ..states.logic import HeroState
from ..style import boton_style, hero_style, hero_titulo_style


def hero() -> rx.Component:

    return rx.box(
        rx.vstack(
            rx.heading(
                HeroState.current_text,
                style=hero_titulo_style
            ),
            rx.text(
                "Desarrollo soluciones digitales que combinan diseño, funcionalidad y una experiencia unica.",
                width="450px",
                align="left"
            ),
            rx.button(
                "Contactame ➡",
                style=boton_style
            )

        ),
        style=hero_style,
    )
