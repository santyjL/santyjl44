import reflex as rx
from ..states.lista_proyectos import caracteristicas_plan_basico, caracteristicas_plan_premium, caracteristicas_plan_profesional
from ..style import (
    Colors, servicios_seccion,precios_style,
    proceso_seccion,card_servicios,ofrezco_servicio_style,
    Font, card_precios, boton_style
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
    return rx.vstack(
        rx.box(
            rx.text(
                num,
                font_size="1.3em",
                width="32px",
                height="32px",
                border_radius="50%",
                color=Colors.PAPER.value,
                bg=Colors.ACCENT.value,
            ),
            text_align="center"
        ),
        rx.vstack(
            rx.heading(titulo, font_size="1.1em"),
            rx.text(descripcion,position="relative", top="-10px", opacity=0.7)
        ),
        style=card_servicios
    )

def precios_cards(
    nombre:str,
    precio:int,
    caracteristicas:list[str],
    borde_color="#999",
    bg=Colors.PAPER.value,
    color=Colors.TEXT_DARK.value
    ) -> rx.Component:

    return rx.vstack(
        rx.text(
            nombre,
            font_family=Font.TITLE.value,
            font_size="2em",
            weight="bold",
            color=Colors.ACCENT.value
        ),
        rx.text(
            f"${precio}",
            font_size="4em"
        ),
        rx.box(
            *[
            rx.hstack(
                rx.text(
                "✔",
                ),
                rx.text(
                caracteristica,
                font_size="1em"
                )
            )
            for caracteristica in caracteristicas
            ]
        ),
        style=card_precios,
        bg= bg,
        border_top=f"3px solid {borde_color}",
        border_bottom=f"2px solid {borde_color}",
        color=color
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
                        descripcion="páginas personalizadas y relevantes donde los visitantes se convierten en nuevos clientes"
                    ),
                    contenido_cards_servicios(
                        icon="building-2",
                        titulo="Sitios Empresariales",
                        descripcion="Webs profesionales que reflejan la identidad de la marca"
                    ),
                    contenido_cards_servicios(
                        icon="square-user-round",
                        titulo="Portafolios",
                        descripcion="Muestra tus trabajos de forma clara, atractiva y profesional"
                    ),
                    contenido_cards_servicios(
                        icon="unlink",
                        titulo="Link Bios",
                        descripcion="páginas de enlaces personalizados para centralizar tu presencia ONLINE"
                    ),
                    displey="flex",
                    flex_flow="row wrap"
                ),
                style=servicios_seccion
            ),
            rx.flex(
                rx.box(
                    rx.center(
                        precios_cards(
                            nombre="Basico",
                            precio=70,
                            caracteristicas = caracteristicas_plan_basico
                        ),
                        precios_cards(
                            nombre="Profesional",
                            precio=120,
                            caracteristicas = caracteristicas_plan_profesional,
                            borde_color=Colors.ACCENT.value,
                            bg= Colors.DESTACAR_CLARO.value
                        ),
                        precios_cards(
                            nombre="Premium",
                            precio=180,
                            caracteristicas = caracteristicas_plan_premium,
                            borde_color=Colors.COFFEE_DARK.value,
                            bg= Colors.COFFEE.value,
                            color=Colors.TEXT_LIGHT.value
                        ),
                        displey="flex",
                        flex_flow="row wrap",

                    ),
                    style=precios_style
                ),
                width="100%"
            ),
            rx.flex(
            rx.box(
                titulo_card_trabajo(
                    "rocket",
                    "Mi Proceso De Trabajo",
                    "Simple, claro y efectivo"
                ),
                rx.center(
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
                        descripcion="Entrego tu página, desplegada y con soporte para que todo funcione perfectamente"
                    ),  
                    displey="flex",
                    flex_flow="row wrap"
                )
                
            ),
            style=proceso_seccion
            ),
            style=ofrezco_servicio_style,
            id="servicios"
        ), 
    )

