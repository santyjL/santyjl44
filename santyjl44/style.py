from enum import Enum
import reflex as rx



class Colors(Enum):
    # ==================================================
    # PALETA PRINCIPAL - CAFETERÍA
    # ==================================================

    ACCENT = "#A5502A"        # Terracota
    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    BACKGROUND = "#F2E8D8"    # Fondo principal
    WHITE = "#F8F4EE"
    BLACK = "#000000"
    NAVBAR = "#2E1A1298"
    LINEAS = "#A5502A"
    DESTACAR = "#D38A3A"
    DESTACAR_CLARO = "#D38A3A70"

    # ==================================================
    # COLORES ADICIONALES
    # ==================================================

    SURFACE_DARK = "#140D09"
    SURFACE_LIGHT = "#F2E8D8"

    TEXT_LIGHT = "#F8F4EE"
    TEXT_DARK = "#2A1D17"

    COFFEE_BLACK = "#140D09"
    COFFEE_DARK = "#2E1A12"
    COFFEE = "#5A3420"

    VERDE= "#25D366"

    PAPER = "#F2E8D8"
    PAPER_DARK = "#E6D8C5"


class Font(Enum):
    # Tipografías

    TITLE = "'Cormorant Garamond', serif"
    TEXT = "'Lora', serif"
    HANDWRITING = "'Caveat', cursive"

    # Colores de texto
    TEXT_PRINCIPAL_COLOR = "#F5F2EC"
    TEXT_DARK = "#2A1D17"

TABLET = "@media screen and (max-width: 1024px)"
MOBILE = "@media screen and (max-width: 768px)"
MOBILE_SM = "@media screen and (max-width: 480px)"


def combinar_estilos(*estilos: dict) -> dict:
    resultado: dict = {}
    for estilo in estilos:
        for clave, valor in estilo.items():
            if (
                isinstance(clave, str)
                and clave.startswith("@media")
                and clave in resultado
                and isinstance(resultado[clave], dict)
                and isinstance(valor, dict)
            ):
                resultado[clave] = {**resultado[clave], **valor}
            else:
                resultado[clave] = valor
    return resultado

fondo = dict(
    bg="""
    radial-gradient(
        circle at center,
        rgba(211,138,58,0.08),
        rgba(90,52,32,0.06),
        transparent
    )
    """,
    animation="respirar 30s ease-in-out infinite"
)

body = dict(
    bg="transparent",
    color=Colors.TEXT_LIGHT.value,
    width="100%",
    max_width="1440px",
    border_left=f"1px solid {Colors.LINEAS.value}",
    border_right=f"1px solid {Colors.LINEAS.value}",
    margin="0 auto",
    font_family=Font.TEXT.value,
)

navbar_style = {
    "background": Colors.NAVBAR.value,
    "backdrop_filter": "blur(12px)",
    "width": "80%",
    "height": "60px",
    "padding": "0.5rem 1rem",
    "position": "fixed",
    "top": "10px",
    "left": "50%",
    "transform": "translateX(-50%)",
    "border_radius": "50px",
    "z_index": "100",
    "border": f"1px solid {Colors.DESTACAR_CLARO.value}",

    TABLET: {
        "width": "90%",
    },

    MOBILE: {
        "top":"0",
        "align":"center",
        "width": "100%",
        "height": "55px",
        "border_radius": "0",
        "padding": "0.5rem 1rem",
    },
}

hero_style = {
    "background_image": f"""
    linear-gradient(
        to right,
        rgba(28,18,13,0.15),
        rgba(28,18,13,0.95)
    ),
    url('{rx.asset("hero.png")}')
    """,

    "background_size": "cover",
    "background_position": "center",
    "color": Colors.WHITE.value,
    "margin": 0,
    "padding": "40px",
    "width": "100%",
    "height": "100vh",
    "border_bottom": f"1px solid {Colors.LINEAS.value}",
    "text_align": "right",
    "display": "flex",
    "justify_content": "flex-end",
    "align_items": "center",

    TABLET: {
        "padding": "0 20px",
    },

    MOBILE: {
        "justify_content": "center",
        "text_align": "center",
        "padding": "0 20px",
    },
}

hero_texto_style={
    "width":"450px",
    "align":"left",

    MOBILE: {
        "width":"300px",
        "align":"center",
    },
}

hero_titulo_style = {
    "animation": "blink 0.8s infinite",
    "border_right": f"5px solid {Colors.DESTACAR.value}",
    "font_size": "4.5em",
    "font_family": Font.TITLE.value,
    "height": "50px",
    "position": "relative",
    "top": "-20px",

    TABLET: {
        "font_size": "4em",
    },

    MOBILE: {
        "font_size": "3em",
        "height": "35px",
        "align":"center",
    },

    MOBILE_SM: {
        "font_size": "2.4em",
        "height": "28px",
        "align":"center",
    },
}

sobre_mi_style = {
    "background": Colors.PAPER.value,
    "color": Colors.TEXT_DARK.value,
    "justify_items": "center",
    "text_align": "justify",
    "padding": "4rem",
    "min_width": "45%",
    "margin": "0 50px",
    "font_family": Font.TEXT.value,

    TABLET: {
        "padding": "2rem",
        "margin": "0",
    },

    MOBILE: {
        "min_width": "100%",
        "margin": "0",
        "padding": "2rem",
    },
}

boton_style = {
    "background_color": Colors.DESTACAR.value,
    "color": Colors.WHITE.value,
    "padding": "20px 70px",
    "border_radius": "10px",
    "margin":"auto",

    MOBILE: {
        "width": "70%",
        "padding": "18px 20px",
        "margin" :"auto"
    },

    "_hover": {
        "background_color": Colors.DESTACAR_CLARO.value,
        "color": Colors.TEXT_DARK.value,
    },
}

boton_whatsApp=dict(
    border=f"2px solid {Colors.VERDE.value}",
    bg="transparent",
    color="white",
    width="100%",
    font_family=Font.TEXT.value,
)

contenido_modal_contacto = {
    "max_width": "900px",
    "background": Colors.COFFEE_DARK.value,
    "padding": "2rem",

    MOBILE: {
        "max_width": "95vw",
        "padding": "1rem",
    },
}

foto_sobre_mi_style = {
    "object_fit": "cover",
    "max_width": "85%",
    "margin": "50px",
    "border_radius": "20px",
    "filter": "brightness(0.85)",

    MOBILE: {
        "max_width": "80%",
        "margin": "auto",
    },
}

foto_datos_style = {
    "background_color": Colors.COFFEE.value,
    "backdrop_filter": "blur(12px)",
    "color": Colors.TEXT_LIGHT.value,
    "padding": "1rem 1.25rem",
    "display": "flex",
    "flex_flow": "row nowrap",
    "align-self":"center",
    "align_items": "center",
    "justify_content": "center",
    "gap": "1rem",
    "border_radius": "10px",
    "height": "80px",
    "width": "80%",


    MOBILE: {
        "position": "relative",
        "left": "auto",
        "bottom": "auto",
        "width": "80%",
        "margin": "1.5rem auto 0 auto",
        "height": "auto",
        "padding": "0.75rem 1rem",
        "justify_content": "space-around",
        "gap": "0.5rem",
        "border_radius": "12px",
    },

    MOBILE_SM: {
        "flex_flow": "row wrap",
        "gap": "0.75rem",
        "padding": "0.75rem 0.5rem",
    },
}

cv_descarga_style= dict(
    bg="transparent",
    border=f"1px solid {Colors.DESTACAR.value}",
    color=Colors.WHITE.value,
    padding="20px 10px",
    border_radius="10px",
    cursor="pointer",
    transition="all .3s ease",
    margin="15px 0",
    font_family=Font.TEXT.value,
    font_weight="bold",
    _hover={
        "border" : f"1px solid {Colors.WHITE.value}",
        "color" : Colors.DESTACAR.value
    }
)

sobre_mi_seccion_style = {
    "display": "flex",
    "flex_flow": "row nowrap",
    "position": "relative",
    "background": Colors.PAPER.value,
    "padding": "150px 0 100px 0",

    TABLET: {
        "flex_flow": "column nowrap",
    },

    MOBILE: {
        "flex_flow": "column nowrap",
        "padding": "100px 0 60px 0",
    },
}

footer_style = {
    "background": Colors.SURFACE_DARK.value,
    "color": Colors.WHITE.value,
    "padding": "2em",

    MOBILE: {
        "padding": "1.5rem",
        "text_align": "center",
    },
}
buttons_style = dict[str, str](
    background=Colors.ACCENT.value,
    color=Colors.WHITE.value,
    padding="0.75rem 1.5rem",
    border_radius="0.5rem",
    cursor="pointer",
)

seo_style = dict[str, str]()

servicios_seccion = {
    "width": "90%",
    "min_height": "400px",
    "background": Colors.PAPER_DARK.value,
    "border_radius": "20px",
    "padding": "2rem",

    TABLET: {
        "width": "45%",
    },

    MOBILE: {
        "width": "100%",
    },
}

proceso_seccion = {
    "width": "100%",
    "margin": "0",
    "min_height": "400px",
    "background": Colors.PAPER.value,
    "padding": "2rem",

    TABLET: {
        "width": "100%",
    },

    MOBILE: {
        "width": "100%",
    },
}

card_servicios = {
    "height" : "200px",
    "padding": "10px",
    "margin" : "0.5em",
    "width" : "23%",
    "background-color" : Colors.PAPER.value,
    "border_radius" : "20px",
    TABLET: {
            "width": "100%",
        },

    MOBILE: {
        "width": "100%",
    },
}

ofrezco_servicio_style = dict(
    overflow="hidden",
    background=Colors.PAPER_DARK.value,
    color=Colors.TEXT_DARK.value,
    width="100%",
    margin= 0,
    display="flex",
    gap="80px",
    flex_flow="row wrap",
    justify_content="center",
    padding="150px 0 40px 0",
)

proyectos_style = {
    "width": "400px",
    "height": "250px",

    TABLET: {
        "width": "320px",
        "height": "220px",
    },

    MOBILE: {
        "width": "280px",
        "height": "180px",
    },
}

proyecto_modal = {
    "background_color": Colors.COFFEE_DARK.value,
    "color": Colors.TEXT_LIGHT.value,
    "padding": "2em",
    "max_width": "800px",
    "height": "90vh",

    MOBILE: {
        "max_width": "95vw",
        "padding": "1rem",
    },
}

titulo_modal = {
    "font_family": Font.TITLE.value,
    "font_size": "2.5em",

    MOBILE: {
        "font_size": "1.8em",
    },
}

imagen_proyecto_modal = {
    "width": "100%",
    "height": "300px",
    "object-fit": "cover",

    MOBILE: {
        "height": "150px",
        "object-fit": "cover",
    },
}

botones_modal = {
    "display": "flex",
    "flex_flow": "row nowrap",
    "justify_content": "space-between",

    MOBILE: {
        "flex_flow": "column nowrap",
        "gap": "10px",
    },
}

proyecto_card_style = dict(
    overflow="hidden",
    background=Colors.PAPER_DARK.value,
    color=Colors.TEXT_DARK.value,
    padding="30px 0 0 0"
)

proyectos_carrusel_style = dict(
    display="flex",
    gap="20px",
    width="max-content",
    padding="2rem 0",
    animation="scroll_projects 15s linear infinite",
)

proyectos_carrusel_barra = dict(
    width="100%",
    position="relative",
    display="flex",
    flex_flow="row nowrap",
    justify_content="space-between",
    padding="0 10px",
    background_color=Colors.PAPER_DARK.value,
    
)

contacto_style = {
    "align_items": "center",
    "color": Colors.BLACK.value,
    "flex-flow":"row wrap",
    "background": Colors.PAPER_DARK.value,
    "padding": "150px 0",

}
