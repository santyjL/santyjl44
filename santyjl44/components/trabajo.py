import reflex as rx

from ..style import (
    Colors, card_trabjo,me_diferencia_style,
    )

def titulo_card_trabajo(icon, titulo, subtitulo) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(
                tag=icon,
                width="32px",
                height="32px",
                color=Colors.COFFEE.value,
            ),
            bg=Colors.PAPER_DARK.value,
            padding="0.5em",
            border_radius="50%"
        ),
        rx.vstack(
            rx.heading(titulo, font_size="1.5em"),
            rx.text(subtitulo, position="relative", top="-10px")
        ),
        margin_bottom="20px",
        border_bottom="1px solid #111",
    )

def contenido_cards_servicios(icon, titulo, descripcion) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(
                tag=icon,
                width="32px",
                height="32px",
                color=Colors.ACCENT.value,
            ),
            bg=Colors.PAPER_DARK.value,
            padding="0.3em",
            border_radius="50%"
        ),
        rx.vstack(
            rx.heading(titulo, font_size="1.1em"),
            rx.text(descripcion,position="relative", top="-10px", opacity=0.7)
        )
    )

def contenido_cards_proceso(num, titulo, descripcion) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                num,
                font_size="1.3em",
                width="32px",
                height="32px",
                color=Colors.PAPER.value,
            ),
            bg=Colors.ACCENT.value,
            padding="0.3em",
            text_align="center",
            border_radius="50%"
        ),
        rx.vstack(
            rx.heading(titulo, font_size="1.1em"),
            rx.text(descripcion,position="relative", top="-10px", opacity=0.7)
        )
    )

def contenido_cards_tecnologias(icon, nombre) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=icon,
                font_size="1.3em",
                width="32px",
                height="32px",
                color=Colors.PAPER.value,
            ),
            rx.heading(
                nombre,
                font_size="1.1em"
            ),
            bg=Colors.ACCENT.value,
            padding="0.3em",
            text_align="center",
            border_radius="10px",
            margin_bottom="5px"
        ),
    )

def me_diferencia () -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                titulo_card_trabajo(
                    "shopping-bag",
                    "Servicios Que Ofrezco",
                    "Soluciones digitales a medida"
                ),
                contenido_cards_servicios(
                    icon="monitor",
                    titulo="Landing Pages",
                    descripcion="Paginas personalizadas y relevantes donde los visitantes se convierten en nuevos clientes"
                    ),
                contenido_cards_servicios(
                    icon="building-2",
                    titulo="Sitios Empresariales",
                    descripcion="Webs profecionales que reflejan la identidad de la marca"
                    ),
                contenido_cards_servicios(
                    icon="square-user-round",
                    titulo="Porfolios",
                    descripcion="Muestra tus trabajos de forma clara, atractiva y profecional"
                    ),
                contenido_cards_servicios(
                    icon="unlink",
                    titulo="Link Bios",
                    descripcion="Paginas de enlaces personalizados para centralizar tu presencia ONLINE"
                    ),
                style=card_trabjo
            ),
            rx.box(
                titulo_card_trabajo(
                    "rocket",
                    "Mi Proceso De Trabajo",
                    "Simple, claro y efectivo"
                ),
                contenido_cards_proceso(
                    num=1,
                    titulo="Descubrimiento",
                    descripcion="Analizo tu idea, necesidades y objetios para entender tu proyecto"
                    ),
                contenido_cards_proceso(
                    num=2,
                    titulo="Diseño y Planificacion",
                    descripcion="Estructuro la infomarcion  y diseño el UI/UX"
                    ),
                contenido_cards_proceso(
                    num=3,
                    titulo="Desarrollo",
                    descripcion="Desarrollo tu web con codigo limpio , rapido y escalable"
                    ),
                contenido_cards_proceso(
                    num=4,
                    titulo="Entrega y Soporte",
                    descripcion="Entrego tu Pagina, desplegada y con soporte para que todo funcione perfectamente"
                    ),
            style=card_trabjo
            ),
            rx.box(
                titulo_card_trabajo(
                    "code-xml",
                    "Tecnologias Que Uso",
                    "Herramientas para crear soluciones"
                ),
                contenido_cards_tecnologias("https://cdn-icons-png.flaticon.com/128/5968/5968544.png", "python"),
                contenido_cards_tecnologias("https://cdn-icons-png.flaticon.com/128/152/152843.png", "HTML5"),
                contenido_cards_tecnologias("https://cdn-icons-png.flaticon.com/128/11518/11518868.png", "Git"),
                contenido_cards_tecnologias("https://cdn-icons-png.flaticon.com/128/732/732007.png", "CSS3"),
                contenido_cards_tecnologias("https://cdn-icons-png.flaticon.com/128/733/733609.png", "GitHub"),
                contenido_cards_tecnologias("https://cdn-icons-png.flaticon.com/128/2930/2930014.png", "Apis"),
                contenido_cards_tecnologias(rx.asset("cursor.svg"), "Cursor IDE"),
                contenido_cards_tecnologias(rx.asset("reflex_icon.svg"), "Reflex Framework"),

                style=card_trabjo
            ),
            style=me_diferencia_style,
            id="servicios"
        ), 
    )

