import reflex as rx

from ..style import (
    Colors, servicios_seccion,proceso_seccion,card_servicios,ofrezco_servicio_style,Font
    )

def titulo_card_trabajo(icon, titulo, subtitulo) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(
                tag=icon,
                width="48px",
                height="48px",
                color=Colors.DESTACAR.value,
            ),
            bg=Colors.PAPER_DARK.value,
            padding="0.8em",
            border_radius="50%"
        ),
        rx.vstack(
            rx.heading(
                titulo,
                font_size="2em",
                color=Colors.TEXT_DARK.value,
                font_family=Font.TITLE.value,
                ),
            rx.text(subtitulo, font_size="1.1em", position="relative", top="-10px")
        ),
        padding="0.4em 0",
        margin_bottom="20px",
        border_bottom="1px solid #111",
        border_radius="10px 10px 0 0",
        color=Colors.DESTACAR.value,
    )



def contenido_cards_servicios(icon, titulo, descripcion) -> rx.Component:
    return rx.box(
        rx.box(
            rx.icon(
                tag=icon,
                width="32px",
                height="32px",
                color=Colors.ACCENT.value,
            ),
            bg=Colors.PAPER_DARK.value,
            padding="0.3em",
            border_radius="50%",
            width="48px",
            height="48px",
            ),
            rx.vstack(
                rx.heading(titulo, font_size="1.1em"),
                rx.text(
                    descripcion,
                    position="relative",
                    top="-10px",
                    opacity=0.7
                )
        ),
        style=card_servicios
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

def ofrezco_servicio () -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(
                titulo_card_trabajo(
                    "shopping-bag",
                    "Servicios Que Ofrezco",
                    "Soluciones digitales a medida"
                ),
                rx.center(
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
                    displey="flex",
                    flex_flow="row wrap"
                ),
                
                style=servicios_seccion
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
            style=proceso_seccion
            ),
            style=ofrezco_servicio_style,
            id="servicios"
        ), 
    )

