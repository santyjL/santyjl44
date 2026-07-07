import reflex as rx

from ..states.logic import HeroState
from ..components.contacto import boton_contacto
from ..style import hero_style, hero_titulo_style, hero_texto_style, cv_descarga_style


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
                "Sitios webs modernos que transmiten Confianza y ayudan a convertir visitantes en clientes reales.",
                style=hero_texto_style
            ),
            rx.flex(
                boton_contacto(),
                cv_descarga(),
                flex_flow="row wrap"
            )

        ),
        style=hero_style,
    )
