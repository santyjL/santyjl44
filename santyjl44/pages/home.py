import reflex as rx

from ..components.navbar import navbar
from ..components.hero import hero
from ..components.footer import footer
from .. components.contacto import contacto
from ..components.sobre_mi import sobre_mi
from ..components.trabajo import me_diferencia
from ..components.proyectos_carrusel import proyectos_carrusel
from ..style import body, fondo


def home() -> rx.Component:
    return rx.center(
        navbar(),
        rx.box(
            hero(),
            sobre_mi(),
            proyectos_carrusel(),
            me_diferencia(),
            contacto(),
            footer(),
            style=body
        ),
        style=fondo
    )
