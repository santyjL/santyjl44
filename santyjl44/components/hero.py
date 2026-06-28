from turtle import right
import reflex as rx

from ..states.logic import HeroState
from ..style import boton_style, hero_style


def hero() -> rx.Component:

    return rx.box(
        rx.vstack(
            rx.heading(
                HeroState.current_text,
                animation="blink 0.8s infinite",
                border_right="5px solid #D38A3A",
                size="9",
                height="60px",
                positon="relative",
                right="180px"
            ),
            rx.text(
                "Desarrollo soluciones digitales que combinan diseño, funcionalidad y una experiencia unica.",
                width="400px",
                align="left"
            ),
            rx.button(
                "Contactame ➡",
                style=boton_style
            )

        ),
        style=hero_style,
    )
