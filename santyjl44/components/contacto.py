import reflex as rx

from ..states.logic import ContactState
import os
from dotenv import load_dotenv
from ..style import (
    contacto_style, boton_style,boton_whatsApp,
    contenido_modal_contacto, Colors, Font
)

load_dotenv()

FORMSPREE = os.getenv("FORMSPREE")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

def boton_contacto() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                "Contáctame ➜",
                style=boton_style,
            )
        ),

        rx.dialog.content(

            rx.heading(
                "Hablemos de tu proyecto ☕",
                margin_bottom="1rem",
                font_family=Font.TITLE.value,
                color=Colors.DESTACAR.value,
            ),

            rx.flex(
                rx.form(
                    rx.vstack(
                        rx.text(
                            "Cuéntame qué necesitas y me pondré en contacto contigo.",
                            font_family=Font.TEXT.value
                        ),
                        rx.input(
                            name="nombre",
                            placeholder="Tu nombre",
                            required=True,
                        ),
                        rx.input(
                            name="email",
                            placeholder="Tu correo electrónico",
                            type="email",
                            required=True,
                        ),
                        rx.text_area(
                            name="mensaje",
                            placeholder="Describe tu proyecto...",
                            min_height="150px",
                            required=True,
                        ),
                        rx.button(
                            "Enviar mensaje",
                            type="submit",
                            style=boton_style,
                            width="100%",
                        ),

                        width="100%",
                        align="stretch",
                        spacing="3",
                    ),

                    on_submit=ContactState.enviar_formulario,
                    reset_on_submit=True
                ),
                rx.vstack(
                    rx.hstack(
                        rx.icon("message_circle", color=Colors.VERDE.value),
                        rx.heading(
                            "WhatsApp",
                            font_size="1.5em",
                            font_family=Font.TITLE.value,
                            color=Colors.VERDE.value,
                            size="5"
                        ),
                    ),
                    rx.text(
                        """
                        ¿Prefieres una conversación más rápida?
                        Escríbeme directamente por WhatsApp.
                        """,
                        font_family=Font.TEXT.value,
                        color="white",
                    ),
                    rx.button(
                        "Abrir WhatsApp",
                        style=boton_whatsApp,
                        on_click=rx.redirect(
                            f"https://wa.me/{WHATSAPP_NUMBER}",
                            is_external=True
                        )
                    ),
                    justify="center",
                    width="40%",
                    height="100%",
                    padding="2rem",
                    border_left=f"1px solid {Colors.LINEAS.value}",
                ),
                width="100%",
                gap="1rem",
                align="stretch",
            ),
            rx.dialog.close(
                rx.icon_button(
                    "x",
                    position="absolute",
                    top="15px",
                    right="15px",
                    bg=Colors.ACCENT.value
                )
            ),
            style=contenido_modal_contacto
            
        ),
    )

def contacto() -> rx.Component:
    return rx.center(
        rx.flex(
            rx.box(
                rx.icon(
                    tag="rocket",
                    width="38px",
                    height="38px",
                    align="center",
                    color=Colors.COFFEE.value,
                ),
                bg=Colors.PAPER.value,
                padding="0.5em",
                width="56px",
                height="56px",
                align_items="center",
                border_radius="50%"
            ),
            rx.vstack(
                rx.heading(
                    "¿Tienes Un Proyecto En Mente?",
                    font_size="1.8em",
                    font_family=Font.TITLE.value
                    ),
                rx.text(
                    "Estoy listo para ayudarte a hacerlo realidad",
                    position="relative",
                    top="-10px",
                    opacity=0.7
                )
            ),
            boton_contacto(),
            flex_flow="row wrap",
            justify_content="center"
            
        ),
        style=contacto_style,
        id="contacto"
    )