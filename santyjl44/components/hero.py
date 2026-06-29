import reflex as rx

from ..states.logic import HeroState
from ..components.contacto import boton_contacto
from ..style import hero_style, hero_titulo_style, cv_descarga_style


def cv_descarga() -> rx.Component:
    return rx.button(
        "Mi Curriculum Vitae",
        style=cv_descarga_style,
        on_click=rx.redirect(
            rx.asset("cv.pdf"),
            is_external=True,
        ),
    )

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
            rx.hstack(
                boton_contacto(),
                cv_descarga()
            )

        ),
        style=hero_style,
    )
